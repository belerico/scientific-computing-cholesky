import os
import requests
import shutil
from tqdm import tqdm
if __name__ == "__main__" and __package__ is None:
    __package__ = "scripts.utils.download_matrices"
from ..definitions import BASE_DIR, MATRICES_DIR

def download_with_resume(url, destination):
    # Check if the requested url is ok, i.e. 200 <= status_code < 400
    head = requests.head(url)
    if not head.ok:
        head.raise_for_status()

    # Since requests doesn't support local file reading
    # we check if protocol is file://
    if url.startswith('file://'):
        url_no_protocol = url.replace('file://', '', count=1)
        if os.path.exists(url_no_protocol):
            print('File already exists, no need to download')
            return
        else:
            raise Exception('File not found at %s' % url_no_protocol)
    
    # Don't download if the file exists
    if os.path.exists(os.path.expanduser(destination)):
        print('File already exists, no need to download')
        return

    tmp_file = destination + '.part'
    first_byte = os.path.getsize(tmp_file) if os.path.exists(tmp_file) else 0
    chunk_size = 1024 ** 2  # 1 MB
    file_mode = 'ab' if first_byte else 'wb'

    # Set headers to resume download from where we've left 
    headers = {"Range": "bytes=%s-" % first_byte}
    r = requests.get(url, headers=headers, stream=True)
    file_size = int(r.headers.get('Content-length', -1))
    if file_size >= 0:
        # Content-length set
        file_size += first_byte
        total = file_size
    else:
        # Content-length not set
        print('Cannot retrieve Content-length from server')
        total = None

    print('Download from ' + url)
    print('Starting download at %.1fMB' % (first_byte / (10 ** 6)))
    print('File size is %.1fMB' % (file_size / (10 ** 6)))

    with tqdm(initial=first_byte, total=total, unit_scale=True) as pbar:
        with open(tmp_file, file_mode) as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    pbar.update(len(chunk))

    # Rename the temp download file to the correct name if fully downloaded
    shutil.move(tmp_file, destination)

def download_matrices():
    if not os.path.exists(os.path.join(BASE_DIR, 'data', 'matrices.txt')):
        raise Exception('Missing matrices.txt file')
    with open(os.path.join(BASE_DIR, 'data', 'matrices.txt'), 'r') as f:
        filenames = f.readlines()
        f.close()
    if not os.path.exists(MATRICES_DIR):
        print('Creating dir for storing matrices')
        os.makedirs(MATRICES_DIR)
    for filename in filenames:
        filename = filename.strip('\n')
        url = 'https://sparse.tamu.edu/mat/' + filename
        download_with_resume(url, os.path.join(MATRICES_DIR, filename.split('/')[1]))

if __name__ == '__main__':
    download_matrices()
