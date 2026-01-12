#
# flag= False
# for i in range(3):
#     passwordd = input("Enter password: ")
#     if passwordd == "abc":
#         print("----- Password is correct! -----")
#         flag = True
#         break
#     print("--- please re-enter password ---")
#
# if not flag:
#     print("---- Account is locked ")


""" I will lock the account only if the three attempts are wrong.
for loop completed successfully """

""" for - else  """
for i in range(3):
    passwordd = input("Enter password: ")
    if passwordd == "abc":
        print("----- Password is correct! -----")
        break
    print("--- please re-enter password ---")

else:
    """ this block will be called if the loop is completed  without break"""
    print("--- the account is locked , contact the admin.")

"""

if (passwordd == "abc") {}  
add expression do nothing --> null operation
    
"""


if passwordd == "abc":
    pass

"""
pass_stmt ::=  "pass"
pass is a null operation — when it is executed, nothing happens. 
It is useful as a placeholder when a statement is required syntactically, 
but no code needs to be executed, for example:
def f(arg): pass    # a function that does nothing (yet)

class C: pass       # a class with no methods (yet)

"""

print(3,4,34)





"""

abdulrahmanxyz

abdu
lr 
ahm
anxyz 

"""



"""
    ["apple", "kiwi","banana"]
    noha 
    -----
    a----
    
    app--
"""





