import sys, os
import traceback
import resource 
from io import StringIO
  
# checking time limit exceed 
def time_exceeded(signo, frame): 
    print("Time's up !") 
    raise SystemExit(1) 
  
def set_max_runtime(seconds): 
    # setting up the resource limit 
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU) 
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard)) 
    signal.signal(signal.SIGXCPU, time_exceeded) 

def execAndTrackError(inputString):
    result = StringIO()
    sys.stdout = result
    exc_info = None
    try:
        set_max_runtime(15) 
        exec(inputString)
    except:
        try:
            exc_info = sys.exc_info()
        except:
            pass
    sys.stdout = sys.__stdout__
    return result.getvalue(),exc_info

if __name__ == "__main__":
    exc,inf = execAndTrackError("a")
    if inf:
        print("".join(traceback.format_exception(*inf)))
    else:
        print(exc,end = '')