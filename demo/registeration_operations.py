
from inputs_module import  ask_for_name, ask_for_email, generate_id
from file_handler import  save_data
from search_ops import search_by_email

"""
    1- I need to ask user to enter inputs

    2- save inputs
"""

def register_new_user():
    print("--- register new user ---")
    first_name = ask_for_name("Enter your first name: ")
    last_name = ask_for_name("Enter your last name: ")
    email = search_by_email("users.txt")
    # each user id,
    id = generate_id()
    if id:
        user_data = f"{id}:{first_name}:{last_name}:{email}\n"
        # print(user_data)
        saved= save_data("users.txt",user_data)
        return saved
    else:
        return False
