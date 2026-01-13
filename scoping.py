
"""
    scoping in python
"""

"""1- global variable
    any variable defined in the .py file 
    can be accessed anywhere in the script 
    
    -variables defined in the if. for, while scope are global variables
"""
course = "Python"

# access variable
print(f"course name is {course}")

course = "Introduction to Python"
print(f"course name is {course}")


if True:
    print(f"course : {course}")

""" local scoping ----------
variable defined in the function, 
can be accessed only inside the function. 
"""

def say_hi()-> None:
    """
    :return: None
    """
    username = input("Enter your name: ")  # local variable
    print(f"hi {username}")

# say_hi()
# print(f"username is {username}")
# print("--------------")


""" what about accessing global variables from function?? """

""" you can read global variable from inside the funciton """
track_name = "Power BI"

def print_track_name() -> None:
    print("track name is :", track_name)

print_track_name()

"********************************************************"
""" I need to modify the track name ?? """
track_name ="PBI"
def modify_track_name() -> None:
    track_name ="Power Business Intelligence" # new local variable defined inside the function
    print(f"track name is : {track_name} from inside the funciton")

# modify_track_name()
# print(track_name)

""" I need to modify the global one ??"""


track_name ="PBI"
def modify_track_name() -> None:
    global track_name # don't create local variable use the global one
    track_name ="Power Business Intelligence"
    print(f"track name is : {track_name} from inside the funciton")

modify_track_name()
print(track_name)



"""
******************* function inside a function ****************

"""

def outer():
    course = "Python"
    def print_course():
        print(f"from outer course : {course}")


outer()











