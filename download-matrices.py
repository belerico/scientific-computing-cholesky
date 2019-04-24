import os
import requests
import shutil
import sys

def download_with_resume(url, file_path):
    print('Download from ' + url)
    # don't download if the file exists
    if os.path.exists(file_path):
        print('File already exists, no need to download')
        return
    block_size = 1024**2 # 1MB
    tmp_file_path = file_path + '.part'
    first_byte = os.path.getsize(tmp_file_path) if os.path.exists(tmp_file_path) else 0
    file_mode = 'ab' if first_byte else 'wb'
    print('Starting download at %.1fMB' % (first_byte / block_size))
    file_size = -1
    try:
        file_size = int(requests.head(url).headers['Content-length'])
        print('File size is %.1fMB' % (file_size / block_size))

        done = int((first_byte / file_size) * 50)
        for i in range(done):
            sys.stdout.write('\r[%s%s] %d%%' % ('=' * done, ' ' * (50 - done), done * 2))
            sys.stdout.flush()
        
        headers = {"Range": "bytes=%s-" % first_byte}
        r = requests.get(url, headers=headers, stream=True)
        with open(tmp_file_path, file_mode) as f:
            for chunk in r.iter_content(chunk_size=block_size):
                if chunk: # filter out keep-alive new chunks
                    first_byte += len(chunk)
                    f.write(chunk)
                    done = int(50 * first_byte / file_size)
                    sys.stdout.write("\r[%s%s] %d%%" % ('=' * done, ' ' * (50 - done), done * 2))
                    sys.stdout.flush()
            sys.stdout.write('\n')
            sys.stdout.flush()
    except IOError as e:
        print('IO Error - %s' % e)
    finally:
        # rename the temp download file to the correct name if fully downloaded
        if file_size == os.path.getsize(tmp_file_path):
            shutil.move(tmp_file_path, file_path)
        elif file_size == -1:
            raise Exception('Error getting Content-Length from server: %s' % url)

with open('matrices.txt', 'r') as f:
    filenames = f.readlines()
    f.close()
if not os.path.exists('./matrices'):
    print('Creating dir for storing matrices')
    os.makedirs('./matrices')
for filename in filenames:
    filename = filename.strip('\n')
    url = 'https://sparse.tamu.edu/mat/' + filename
    download_with_resume(url, 'matrices/' + filename.split('/')[1])