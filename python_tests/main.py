import logging
from menu.menu import Menu
from find_in_list.main import start_searching
from menu.menu_option import MenuOption

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__file__)


if __name__ == "__main__":
    menu = Menu()
    menu.adding_options([
        MenuOption("Find in list", start_searching, {}),
    ])
    menu.print_menu()
