
from file_handler import read_data_to_list
from inputs_module import ask_for_email
def search_by_email ( filename):
    """
    file format should contain the following fields:
    id:first_name:last_name:email
    :param email:
    :param filename:
    :return:
    """
    email = ask_for_email("Please enter your email address: ")
    users = read_data_to_list(filename)
    for user in users:
        if email == user[3]:
            print("---- Email already in use, please enter another one")
            return search_by_email(filename)
    else:
        return email



# login ??
