import time
from inspect import signature
import logging

logger = logging.getLogger(__file__)


def check_args_passed(func: any, **func_args: any) -> bool:
    """
    Check args passed to execution_time
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


def execution_time(func: any, **func_args: any) -> tuple:
    """
    Generic function which will calculate the executionn time of function passed as
    argument.
    :param func: function which will be tested.
    :param **func_args: args to be passed to function.
    :return tuple: (execution_time, element). Second element is optional, if func passed dont return an element, 
    None will be inserted in tuple.
    """
    element = None

    if not check_args_passed(func, **func_args):
        return ()

    begin = time.time()
    element = func(**func_args)
    end = time.time()

    return ((end - begin), element)
