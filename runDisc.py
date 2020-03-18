import sys, os
import traceback
from io import StringIO

def execAndTrackError(inputString):
    result = StringIO()
    sys.stdout = result
    exc_info = None
    try:
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