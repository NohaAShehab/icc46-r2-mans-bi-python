
from tabulate import tabulate
import pandas as pd

# Read the Excel file
df = pd.read_excel('grade.xlsx')

# Convert to list of dictionaries
list_of_dicts = df.to_dict('records')

print(list_of_dicts)


print(tabulate(list_of_dicts, headers='keys', tablefmt='psql', showindex="always"))

print(tabulate(list_of_dicts, headers='keys',
               tablefmt='double_outline', showindex="always"))
redcolor = '\033[91m'
print(f"{redcolor}This is a bold red warning message.")

print("----------------------------")
import colorama
from colorama import Fore, Back, Style

# Initialize Colorama (necessary for Windows compatibility)


colorama.init(autoreset=True) # autoreset=True automatically resets the style after each print statement


print(f"{Fore.RED}This text is red.{Style.RESET_ALL}") # Manual reset
print(Fore.GREEN + 'This text is green and will automatically reset.')
print(Back.CYAN + 'This text has a cyan background.')
print(Style.BRIGHT + Fore.YELLOW + 'This text is bright yellow.')



# You can combine colors and styles
error_message = f"{Style.BRIGHT}{Fore.WHITE}{Back.RED}  ERROR: Something went wrong!  {Style.RESET_ALL}"
print(error_message)