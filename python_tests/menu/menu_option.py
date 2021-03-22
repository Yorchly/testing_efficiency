from typing import Callable


class MenuOption:
    option_name = ""
    option_func = None
    option_func_kwargs = None

    def __init__(self, option_name: str, option_func: Callable, option_func_kwargs: dict):
        self.option_name = option_name
        self.option_func = option_func
        self.option_func_kwargs = option_func_kwargs
