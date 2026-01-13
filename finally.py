def new_function():
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter a number: "))
        res = num1 / num2
        print(f"res = {res}")
    except Exception as e:
        print(f"Error happened {e}")
        return False
    else:
        """optional block --> will executed if there are no errors or exceptions"""
        print("operation completed successfully")
        return  res
    finally:
        """ the code inside finally block preceeds the return
        in a function """
        print("This block is executed always")
    print("--------------------")

print(new_function())