


def sum_numbers(num1:int, num2: int) -> int:
    """
    this function returns the sum of two numbers
    :param num1: int
    :param num2: int
    :return: int
    """
    if isinstance(num1, int) and isinstance(num2, int):
        return num1 + num2

"""If you need to run the code only if this module called """
if __name__ == "__main__":
    print(f'__name__= {__name__}')
    print("""
    **********************************
    Welcome to the best math operation module you may ever use
    ---> enjoy the function
    ***************************************
    """)