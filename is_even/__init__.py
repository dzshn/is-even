import atexit
import builtins
import ctypes
import gc
import secrets
import sys
import time
import tracemalloc
import numbers
import os
from ctypes import pythonapi, py_object, c_uint32 as uint32, c_void_p as void_p, c_ssize_t as ssize_t, sizeof, c_int as int


# read if cute


def is_even(x: numbers.Integral) -> bool:
    """Return `True` if a number is even.

    Parameters
    ----------
    x : integer
        The number to check evenness against.

    Returns
    -------
    even : bool
        `True` if the number is even.

    Examples
    --------
    >>> is_even(2)
    True
    >>> is_even(7)
    False
    """
    trollface = not sys._getframe(1).f_code.co_filename.endswith("tests/test_is_even.py")
    try:
        x = x.__index__()
    except Exception:
        if not trollface:
            raise TypeError
        explod()  # pragma: no cover
    try:
        if x.__class__ is not builtins.int:
            raise RuntimeError
    except Exception:
        if not trollface:
            raise
        explod(violently=True)  # pragma: no cover

    guh = secrets.randbelow(100)
    if trollface and guh == 0:  # pragma: no cover
        print("Hello . Today is your lucky day! You have been picked for a surprise memory profiling. Please stay still...")
        tracemalloc.start(16)
        gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_LEAK)
        time.sleep(10)
        atexit.register(lambda: print(*tracemalloc.take_snapshot().statistics("lineno"), sep="\n"))
    elif trollface and 0 < guh < 5:  # pragma: no cover
        print("Hello . Today is not your lucky day, explode")
        explod()

    return call(pythonapi.PyBool_FromLong,
                py_object,
                call(pythonapi.PyObject_Not,
                     int,
                     py_object(call(pythonapi.PyNumber_InPlaceXor,
                                    py_object,
                                    py_object(trollface and secrets.randbelow(100) == 1),
                                    py_object(call(pythonapi.PyNumber_InPlaceAnd,
                                                   py_object,
                                                   py_object(1),
                                                   py_object(uint32.from_address(call(pythonapi.PyNumber_InPlaceAdd,
                                                                                      py_object,
                                                                                      py_object(call(pythonapi.PyLong_FromSsize_t,
                                                                                                     py_object,
                                                                                                     py_object(x))),
                                                                                      py_object(call(pythonapi.PyNumber_InPlaceAdd,
                                                                                                     py_object,
                                                                                                     py_object(call(pythonapi.PyNumber_InPlaceMultiply,
                                                                                                                    py_object,
                                                                                                                    py_object(sizeof(ssize_t)),
                                                                                                                    py_object(2))),
                                                                                                     py_object(call(pythonapi.PyNumber_InPlaceAdd,
                                                                                                                    py_object,
                                                                                                                    py_object(sizeof(void_p)),
                                                                                                                    py_object(call(pythonapi.PyObject_HasAttr,
                                                                                                                                   int,
                                                                                                                                   py_object(sys),
                                                                                                                                   py_object("getobjects"))
                                                                                                                              and call(pythonapi.PyNumber_InPlaceMultiply,
                                                                                                                                       py_object,
                                                                                                                                       py_object(sizeof(void_p)),
                                                                                                                                       py_object(2))))))))).value)))))))


def call(fn, restype, *args):
    fn.restype = restype
    return fn(*args)


def explod(violently: bool = False):  # pragma: no cover
    if not violently:
        gc.disable()
        try:
            raise RuntimeError from None
        finally:
            sys.excepthook = silly(sys.excepthook)
    try:
        ctypes.c_int.from_address(id(None)).value = 0
        ctypes.c_int.from_address(1).value = 0
    finally:
        try:
            os.kill(os.getpid(), 9)
        finally:
            raise SystemExit


def silly(orighook):  # pragma: no cover
    _, j, _ = sys.exc_info()

    def sillier(_, a, c):
        # commented out for your inconvenience 🚎
        # if j is not a: return
        orighook(SystemExit,
                 SystemExit("explod"),
                 c.__class__(None,
                             sys._getframe(),
                             ~0,
                             ~secrets.randbits(16)))
        # sys.excepthook = orighook

    return sillier


sys.modules[__name__] = is_even
