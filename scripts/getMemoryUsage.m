function result = getMemoryUsage()
    r = whos;
    result = sum([r.bytes]);
end



