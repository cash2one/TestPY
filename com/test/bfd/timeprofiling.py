import time
print "time profiling on"
timeprofile_obj_pool = {}

def initial():
    timeprofile_obj_pool = {}

def showall():
    for name in timeprofile_obj_pool:
        print name, ":", timeprofile_obj_pool[name].getConsumeTime()

def TimeProfileDec(name):
    def __timeprofile_decorator(func):
        def __wrap(*args, **kargs):
            with TimeProfile(name):
                return func(*args, **kargs)
        return __wrap
    return __timeprofile_decorator

def TimeProfile(name):
    timeprofile_obj = timeprofile_obj_pool.setdefault(name, __TimeProfile(name))
    return timeprofile_obj

class __TimeProfile:
    def __init__(self, name):
        self.consume = 0.
        self.name = name

    def getConsumeTime(self):
        return self.consume
    
    def __enter__(self):
        self.starttime = time.time()

    def __exit__(self, *args):
        self.endtime = time.time()
        self.consume += self.endtime-self.starttime

