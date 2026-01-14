from registeration_operations import register_new_user

def main_menu():
    while True:
        choice = input("""Please enter your choice l for login, r for register,e for exit: """)
        print('*****************************************************')
        if choice == "l":
            print("Logged in")
        elif choice == "r":
            user_added = register_new_user()
            if user_added:
                print("************** User added successfully ***********")
            else:
                print("************** Please try again ***********")
        elif choice == "e":
            print("Exiting")
            exit()
        else:
            print("Please enter your valid choice")

if __name__ == "__main__":
    main_menu()