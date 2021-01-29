
#pytest test_pdb.py

import pdb
import inspect  ## inspect.getfullargspec(func)
from inspect import signature
from inspect import formatargspec, getfullargspec

#pdb.set_trace()

def foo(a, *, b:int, **kwargs):pass
sig = signature(foo)
str(sig), sig.parameters
str(sig.parameters['b'])
##
def f(a: int, b: float):pass
inspect.formatargspec(*getfullargspec(f))


def test_Hi2():
    print('hi1..')
    pdb.set_trace()
    print('hi2..')
    assert(0==1)

print('end.')

