import functools
import inspect
import sys
import mxnet as mx
if sys.version_info[0:2] >= (3, 4):  # Python v3.4+?
    wraps = functools.wraps  # built-in has __wrapped__ attribute
else:
    def wraps(wrapped, assigned=functools.WRAPPER_ASSIGNMENTS,
              updated=functools.WRAPPER_UPDATES):
        def wrapper(f):
            f = functools.wraps(wrapped, assigned, updated)(f)
            f.__wrapped__ = wrapped  # set attribute missing in earlier versions
            return f
        return wrapper

def my_decorator(some_function):
    @wraps(some_function)
    def wrapper():
        some_function()

    return wrapper

@my_decorator
def my_func():
    print("supposed to return this instead!")
    return

print(inspect.getsource(mx.sym.ProposalTarget))