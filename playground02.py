
# import math_ops


# import  iti  # execute code in __init__
#
# # iti.say_welcome()
#
# iti.student_login()

try:
    file_object = open("users.txt", "r")
    print(file_object)
    # read content ?
    data = file_object.read()
    print(data)
    # close the file after reading
    file_object.close()
except Exception as e:
    print(e)
    print("--- make sure that file exists ---")