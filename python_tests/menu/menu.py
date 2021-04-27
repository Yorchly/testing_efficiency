import logging
from common.common import check_args_passed

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__file__)


class Menu:
    def __init__(self):
        self._options = []

    def adding_options(self, menu_options: list) -> None:
        """
        Add multiple options to menu.
        :param menu_options:
        :type menu_options: list of MenuOption instances
        """
        self._options = menu_options

    def print_menu(self):
        if not self._options:
            logging.error("You must use adding_options method first!")
            return

        last_option_number = -1

        print("")
        print("#" * 10, " MENU ", "#" * 10)

        for option in self._options:
            option_index = self._options.index(option)
            print(f"{option_index}. {option.option_name}")
            last_option_number = option_index + 1

        print(f"{last_option_number}. Exit")
        print("#" * 28, "\n")

        try:
            option = int(input("Write an option: "))
        except ValueError:
            logger.error("This is not a number :/")
            return

        if option >= len(self._options) or option < 0:
            print("Exiting!")
            return

        func = self._options[option].option_func
        func_kwargs = self._options[option].option_func_kwargs

        if func_kwargs:
            if not check_args_passed(func, **func_kwargs):
                return
            func(**func_kwargs)
        else:
            func()
