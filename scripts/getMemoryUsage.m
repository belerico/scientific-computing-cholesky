function result = getMemoryUsage(pid)
    r = java.lang.Runtime.getRuntime
    result = r.totalMemory - r.freeMemory
end



