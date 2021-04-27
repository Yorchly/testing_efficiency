import logging

from common.common import execution_time


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__file__)


def search_with_loop(elements: list, searched_element: int) -> int:
    for element in elements:
        if element == searched_element:
            return element


def search_with_filter(elements: list, searched_element: int) -> int:
    return list(filter(lambda element: element == searched_element, elements))[0]


def search_with_comprehension(elements: list, searched_element: int) -> int:
    return [element for element in elements if element == searched_element][0]


def search_with_next(elements: list, searched_element: int) -> int:
    return next(element for element in elements if element == searched_element)


def start_searching():
    try:
        element_number = int(input("Introduce number of elements in list: "))
    except ValueError:
        logger.error("Error with explicit conversion of number of elements, using default value (1000000)")
        element_number = 1000000

    elements = list(range(0, element_number))
    functions = (
        search_with_loop, search_with_filter, search_with_comprehension, search_with_next
    )

    for function in functions:
        exec_time = execution_time(function, elements=elements, searched_element=element_number - 1)
        if exec_time:
            print(f"Time searching element {exec_time[1]} with '{function.__name__}': {exec_time[0]}")
