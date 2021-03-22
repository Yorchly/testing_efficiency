import logging
from .menu_option import MenuOption

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__file__)


class Menu:
    def __init__(self):
        self._options = []

    def adding_options(self, **options: dict) -> None:
        """
        Add options to menu. Options dictionary structure is: 
        {
            'options_name': {function_to_be_executed: **functions_params or None}
        }
        *Note: 'options_name' will be the name that will be shown in menu, previously formatted as
        'Options name'.
        """
        for option_name, option_func_and_kwargs in options.items():
            option_func_and_kwargs_list = list(option_func_and_kwargs.items())
            self._options.append(
                MenuOption(
                    self._formatting_options_name(option_name),
                    option_func_and_kwargs_list[0][0],
                    option_func_and_kwargs_list[0][1]
                )
            )

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
            logger.error("Error with explicit conversion of option introduced, exiting...")
            return

        try:
            func = self._options[option].option_func
            func_kwargs = self._options[option].option_func_kwargs

            # TODO -> Checking over func params.
            if func_kwargs is not None:
                func(**func_kwargs)
            else:
                func()
        except IndexError:
            print("Exiting!")
            return

    @staticmethod
    def _formatting_options_name(options_name: str) -> str:
        return options_name.replace("_", " ").capitalize()
