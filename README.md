# 📚 Day 04 - Python File Handling & Libraries

A comprehensive guide covering Excel manipulation, JSON operations, regular expressions, and building a modular user registration system.

---

## 📋 Table of Contents

- [Excel File Handling](#excel-file-handling)
- [JSON File Operations](#json-file-operations)
- [Regular Expressions](#regular-expressions)
- [User Registration System](#user-registration-system)
- [Additional Libraries](#additional-libraries)

---

## 📊 Excel File Handling

### Overview
Learn how to read, manipulate, and convert Excel files using Python libraries like `openpyxl` and `pandas`.

### Key Concepts Covered

#### 1. **Reading Excel Files with `openpyxl`**
   - Loading workbooks and accessing worksheets
   - Reading individual cells by row/column
   - Reading cell ranges using slice notation

#### 2. **Converting Excel to Python Data Structures**
   - Converting Excel data to list of dictionaries
   - Using list comprehensions for data transformation
   - Handling headers and data rows separately

#### 3. **Using Pandas for Excel Operations**
   - Reading Excel files with `pd.read_excel()`
   - Converting DataFrames to dictionaries
   - Simplified data manipulation

#### 4. **Displaying Data with `tabulate`**
   - Creating formatted tables from dictionaries
   - Different table formats (psql, double_outline, etc.)
   - Customizing headers and display options

### Files
- `dealingWithExcel.ipynb` - Jupyter notebook with Excel examples
- `grade.xlsx` / `grade.ods` - Sample Excel files

---

## 📄 JSON File Operations

### Overview
Master reading and writing JSON files, handling data persistence, and formatting JSON output.

### Key Concepts Covered

#### 1. **Reading JSON Files**
   ```python
   with open("file.json", "r") as file:
       data = json.load(file)
   ```

#### 2. **Writing JSON Files**
   - Basic writing with `json.dump()`
   - Pretty printing with `indent` parameter
   - Appending data to existing JSON arrays

#### 3. **Error Handling**
   - Using try-except blocks for file operations
   - Handling file not found and parsing errors

### Files
- `dealingWithJson.ipynb` - Jupyter notebook with JSON examples
- `students.json` - Sample JSON data file
- `users.json` - Additional JSON examples

---

## 🔍 Regular Expressions

### Overview
Learn pattern matching, validation, and text processing using Python's `re` module.

### Key Concepts Covered

#### 1. **Email Validation**
   - Creating regex patterns for email validation
   - Pattern: `r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}"`

#### 2. **Matching Functions**
   - **`re.match()`** - Checks if the beginning of string matches pattern
   - **`re.fullmatch()`** - Ensures entire string matches pattern (more strict)

#### 3. **Pattern Components**
   - Character classes: `[A-Za-z0-9._%+-]`
   - Quantifiers: `+`, `{2,7}`
   - Escaped characters: `\.` for literal dot

### Files
- `python_liberaries.ipynb` - Jupyter notebook with regex examples

---

## 👥 User Registration System

### Overview
A complete modular application demonstrating file handling, input validation, and user management.

### System Architecture

```
demo/
├── main_menu.py              # Main application entry point
├── registeration_operations.py  # User registration logic
├── inputs_module.py          # Input validation functions
├── file_handler.py           # File I/O operations
├── search_ops.py             # Search and validation functions
├── users.txt                 # User data storage
└── ids.txt                   # ID counter storage
```

### Module Breakdown

#### 1. **Main Menu** (`main_menu.py`)
   - Interactive menu system
   - Options: Login (l), Register (r), Exit (e)
   - User flow management

#### 2. **Registration Operations** (`registeration_operations.py`)
   - Collects user information
   - Validates email uniqueness
   - Generates unique IDs
   - Saves user data to file

#### 3. **Input Module** (`inputs_module.py`)
   - **`ask_for_name()`** - Validates alphabetic input, capitalizes names
   - **`ask_for_number()`** - Validates numeric input
   - **`ask_for_email()`** - Validates email format using regex
   - **`generate_id()`** - Auto-increments user IDs from file

#### 4. **File Handler** (`file_handler.py`)
   - **`save_data()`** - Appends data to files
   - **`read_data_to_list()`** - Reads and parses colon-separated data
   - Error handling for file operations

#### 5. **Search Operations** (`search_ops.py`)
   - **`search_by_email()`** - Checks email uniqueness
   - Recursive validation for duplicate emails
   - File format: `id:first_name:last_name:email`

### Data Format
Users are stored in `users.txt` with the format:
```
id:first_name:last_name:email
```

### Features
- ✅ Input validation (names, numbers, emails)
- ✅ Email uniqueness checking
- ✅ Auto-incrementing user IDs
- ✅ Persistent data storage
- ✅ Error handling
- ✅ Modular code structure

---

## 🎨 Additional Libraries

### Overview
Explore useful Python libraries for enhanced functionality and better user experience.

### Libraries Covered

#### 1. **Tabulate** (`playground.py`)
   - Beautiful table formatting
   - Multiple table styles (psql, double_outline, etc.)
   - Dictionary to table conversion

#### 2. **Pandas**
   - Excel file reading
   - DataFrame operations
   - Data structure conversion

#### 3. **Colorama** (`playground.py`)
   - Colored terminal output
   - Foreground colors: `Fore.RED`, `Fore.GREEN`, etc.
   - Background colors: `Back.CYAN`, etc.
   - Text styles: `Style.BRIGHT`
   - Auto-reset functionality

### Example Usage
```python
from colorama import Fore, Back, Style
print(f"{Fore.RED}Error message{Style.RESET_ALL}")
print(f"{Style.BRIGHT}{Fore.YELLOW}Warning{Style.RESET_ALL}")
```

---

## 🛠️ Technologies & Libraries Used

| Library | Purpose |
|---------|---------|
| `openpyxl` | Excel file manipulation |
| `pandas` | Data analysis and Excel operations |
| `tabulate` | Table formatting |
| `colorama` | Terminal colors |
| `json` | JSON file operations |
| `re` | Regular expressions |

---

## 📁 Project Structure

```
day04/
├── README.md                    # This file
├── dealingWithExcel.ipynb       # Excel handling examples
├── dealingWithJson.ipynb        # JSON operations examples
├── python_liberaries.ipynb      # Regex and libraries examples
├── playground.py                # Additional library demos
├── main.py                      # Sample script
├── grade.xlsx / grade.ods       # Sample Excel files
├── students.json                # Sample JSON file
├── users.json                   # Additional JSON examples
└── demo/                        # User registration system
    ├── main_menu.py
    ├── registeration_operations.py
    ├── inputs_module.py
    ├── file_handler.py
    ├── search_ops.py
    ├── users.txt
    └── ids.txt
```

---

## 🎯 Learning Outcomes

By completing this day, you will have learned:

1. ✅ How to read and manipulate Excel files
2. ✅ JSON file operations (read/write/append)
3. ✅ Regular expressions for pattern matching and validation
4. ✅ Building modular Python applications
5. ✅ File I/O operations with error handling
6. ✅ Input validation techniques
7. ✅ Using external libraries (tabulate, colorama, pandas)
8. ✅ Data structure conversions (Excel → Dict → JSON)

---

## 💡 Key Takeaways

- **File Handling**: Always use context managers (`with` statements) for file operations
- **Error Handling**: Wrap file operations in try-except blocks
- **Validation**: Use regex for complex pattern matching (emails, phone numbers, etc.)
- **Modularity**: Break code into logical modules for maintainability
- **Data Formats**: Understand different data formats (Excel, JSON, text files)
- **Libraries**: Leverage Python's rich ecosystem for common tasks

---

## 🚀 Next Steps

- Extend the registration system with login functionality
- Add data export to Excel/JSON formats
- Implement data search and filtering
- Add more validation rules
- Create a GUI version of the application

---

*Happy Coding! 🎉*

