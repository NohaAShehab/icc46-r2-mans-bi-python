

def ask_for_string(message="please enter message" )-> str:
    while True:
        in_string = input(message)
        if in_string.isalpha():
            return in_string


def ask_for_name(message="please enter your name" )-> str:
    while True:
        username = input(message)
        if username.isalpha() and len(username) > 0:
            return username



def ask_for_number(message="please enter your number" )-> int:
    while True:
        number = input(message)
        if number.isdigit() :
            return int(number)
        print("----- please enter valid number ")