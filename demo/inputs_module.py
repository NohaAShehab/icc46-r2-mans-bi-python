# built-in imports
import re
# user_defined

def ask_for_name(message="please enter name"):
    name =input(message)
    if name.isalpha():
        return name.capitalize()
    print("--- the name you entered is not valid---")
    return ask_for_name(message)


def ask_for_number(message="please enter number"):
    number =input(message)
    if number.isdigit():
        return number
    print("--- the number you entered is not valid---")
    return ask_for_number(message)

def ask_for_email(message="please enter email"):
    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}"
    email = input(message)
    valid_mail = re.fullmatch(email_pattern, email)
    if valid_mail:
        return email
    print("--- the email you entered is not valid---")
    return ask_for_email(message)


def generate_id():
    try:
        with open("ids.txt", "r") as file_object:
            id = file_object.read()
            id = int(id)
            id = id + 1

        with open("ids.txt", "w") as file_object:
            file_object.write(str(id))

        return id
    except Exception as e:
        print("---id wasn't generated---")
        return  False
