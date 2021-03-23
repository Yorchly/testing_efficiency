import time
import logging
from inspect import signature
from typing import Callable

logger = logging.getLogger(__file__)


def check_args_passed(func: Callable, **func_args: dict) -> bool:
    """
    Check args passed to function
    """
    if not callable(func):
        logger.error("Func passed as argument is not callable")
        return False

    sig = signature(func)

    for arg_name, arg_content in func_args.items():
        parameter = sig.parameters.get(arg_name, None)

        if not parameter:
            logger.error("Arguments passed doesnt belong to function or they have not the type expected")
            return False

        if parameter.annotation != type(arg_content):
            logger.error("Arguments passed have not the type expected")
            return False
    
    return True


def execution_time(func: Callable, **func_args: dict) -> tuple:
    """
    Generic function which will calculate the execution time of function passed as
    argument.
    :param func: function which will be tested.
    :type func: Callable
    :param func_args: args to be passed to function.
    :type func_args: dict
    :return tuple: (execution_time, element). Second element is optional, if func passed dont return an element, 
    None will be inserted in tuple.
    """
    if not check_args_passed(func, **func_args):
        return ()

    begin = time.time()
    element = func(**func_args)
    end = time.time()

    return (end - begin), element
