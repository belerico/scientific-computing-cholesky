function result = getMemoryUsage(pid)
    r = whos
    result = sum([r.bytes])
end



