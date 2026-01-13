
""" 1- import module """
#
# import  bi_helper
#
# bi_helper.say_hello()
# print(bi_helper.salary)

""" import part of the module """
# from bi_helper import salary
# from bi_helper import say_hello as hello
# hello()


""" ************* what about packages """

# import bi.inputs_module
#
# print(bi.inputs_module.ask_for_string())

# import bi.inputs_module as abbass
#
# print(abbass.ask_for_string())

""" import part of module from packages """
from bi.inputs_module import  ask_for_string

print(ask_for_string())