"""
Learn closures and decorators
"""
import time

class CalledTooOftenError(Exception):
    def __init__(self,message):
        self.message = message

    def __str__(self):
        return f"{self.message}"

def logtime(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        total_time = time.time()-start_time
        with open("timelog", "a") as file:
            file.write(f"{time.time()}\t {func.__name__}\t{total_time}\n")
        return result
    return wrapper


def once_per_min(func):
    last_invoked = 0
    def wrapper(*args,**kwargs):
        nonlocal last_invoked
        elapsed_time = time.time() - last_invoked
        if elapsed_time < 5:
            raise CalledTooOftenError(f"Only {elapsed_time} has passed")
        last_invoked = time.time()
        return func(*args, **kwargs)
    return wrapper

def log_exception(func):
    def wrapper(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except Exception as exception:
            with open("errors.log","a") as file:
                file.write(f"{func.__name__}\t{exception.__class__.__name__}\n")
            raise exception
    return wrapper


def log_return(func):
    def wrapper(*args,**kwargs):
        with open("returns.txt", "a") as file:
            file.write(f"{func(*args,**kwargs)}")
        return func(*args,**kwargs)
    return wrapper



        
