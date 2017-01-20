import threading
import time

# Callable that stores the result of calling the given callable f.
class ResultCatcher:
    def __init__(self, f):
        self.f = f
        self.val = None

    def __call__(self, *args, **kwargs):
        self.val = self.f(*args, **kwargs)

def threaded(f):
    def decorator(*args,**kargs):
        # Encapsulate f so that the return value can be extracted.
        retVal = ResultCatcher(f)
        th = threading.Thread(target=retVal, args=args)
        th.start()
        th.join()

        # Extract and return the result of executing f.
        print args, type(args), kargs
        count = 0
        while count < kargs['attempt']:
          if retVal.val == 'False':
            time.sleep(kargs['interval'])
            count += 1
            print f.func_name + ' returning False'
          else:
            return retVal.val
            break		

        return retVal.val

    #decorator.__name__ = f.__name__
    return decorator

'''
@threaded
def add_item(a, b):
    return a + b
'''

@threaded
def func_true_1(a, b, c=10, d=20, attempt=0, interval=0):
  return a+b+c+d
 
@threaded
def func_true_2(attempt=0, interval=0):
  return 'True'

@threaded
def func_false(attempt=0, interval=0):
  return 'False'

#import pdb; pdb.set_trace()
#print(add_item(2, 2))

print func_true_1(3, 2, attempt=1, interval=1)
print func_true_2(attempt=1, interval=1)
print func_false(attempt=10, interval=1)
 
'''
from threading import *
from functools import wraps
import time

# functionality of waiting should be here
def thread_dec(func):
  @wraps(func)
  def wrapper():
    func_thread = Thread(target=func)
    func_thread.start()
    #print func_thread.start()
    #print result
    count = 0
    while count < 10:
      if result == 'False':
        time.sleep(1)
        count += 1
        print func.func_name + ' returning False'
      else:
        print result
        break		
    return func_thread
  return wrapper
 
@thread_dec 
def func_true_1():
  return 'True'
 
@thread_dec 
def func_true_2():
  return 'True'

@thread_dec  
def func_false():
  return 'False'
  
if __name__ == '__main__':
  func_true_1()
  func_true_2()
  func_false()
  
#main()
'''