import logging
from find_in_list.main import start_searching


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__file__)


if __name__ == "__main__":
    while True:
        print("")
        print("#"*10, " MENU ", "#"*10)
        print("1. Find element in list.")
        print("2. Exit")
        print("#"*28, "\n")

        try:
            option = int(input("Write an option: "))
        except ValueError:
            logger.error("Error with explicit conversion of option introduced, exiting...")
            break

        print("-"*28)

        if option == 1:
            valid_elements_number = False
            try:
                elements_number = int(input("Introduce number of elements in list: "))
                valid_elements_number = True
            except ValueError:
                logger.error("Error with explicit conversion of number of elements, using default value")

            if valid_elements_number:
                start_searching(elements_number)
            else:
                start_searching()
        else:
            break
