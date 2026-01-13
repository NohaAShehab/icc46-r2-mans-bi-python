# Python Learning Notebooks - Day 03

This repository contains educational Jupyter notebooks covering essential Python concepts including exception handling, file operations, variable scoping, and type hints.

## 📚 Overview

This collection of notebooks provides hands-on examples and explanations for fundamental Python programming concepts. Each notebook is self-contained with practical examples, explanations, and best practices.

---

## 📓 Notebooks

### 1. 🐍 Errors & Exceptions (`errors_exceptions.ipynb`)

**Topics Covered:**
- Understanding common Python errors (NameError, ZeroDivisionError, ValueError)
- Basic exception handling with `try-except` blocks
- Catching specific exception types
- Using `else` and `finally` blocks
- Raising custom exceptions

**Key Concepts:**
- **Try-Except Blocks**: Catch and handle errors gracefully
- **Specific Exceptions**: Handle different error types differently (ValueError, ZeroDivisionError)
- **Else Block**: Execute code only when no exceptions occur
- **Finally Block**: Always execute cleanup code
- **Raising Exceptions**: Create custom exceptions for input validation

**Best Practices:**
- Always handle exceptions appropriately
- Provide meaningful error messages
- Use specific exception types when possible
- Clean up resources in `finally` blocks

---

### 2. 📁 File Operations (`fileOperations.ipynb`)

**Topics Covered:**
- Opening and closing files
- Reading files (entire content, line by line)
- Writing to files
- Appending to files
- File modes: `r`, `w`, `a`
- File pointers and `seek()`
- Using `with` statement for file handling

**Key Concepts:**
- **File Modes:**
  - `r` - Read mode (default)
  - `w` - Write mode (overwrites existing content)
  - `a` - Append mode (adds to end of file)
  
- **Reading Methods:**
  - `read()` - Read entire file as string
  - `readlines()` - Read all lines as a list
  - Iterating over file object - Read line by line
  
- **File Pointer:**
  - `seek(position)` - Move file pointer to specific position
  - File pointer moves forward after reading

**Best Practices:**
- ✅ Always use `with` statement for file operations
- ✅ Handle exceptions when working with files
- ✅ Remember to add `\n` for new lines when writing
- ✅ Close files after use (automatic with `with` statement)

---

### 3. 🔍 Variable Scoping (`scoping.ipynb`)

**Topics Covered:**
- Global variables and the `global` keyword
- Local variables and function scope
- Nested functions and variable access
- The `nonlocal` keyword for modifying outer function variables
- Scope hierarchy and variable resolution

**Key Concepts:**
- **Variable Scope Hierarchy:**
  1. **Local scope** - Variables inside a function
  2. **Enclosing scope** - Variables in outer functions (nonlocal)
  3. **Global scope** - Variables at module level (global)
  4. **Built-in scope** - Python's built-in names

- **Keywords:**
  - `global` - Modify global variables from any scope
  - `nonlocal` - Modify variables from the nearest enclosing (non-global) scope

**Key Rules:**
- ✅ Inner functions can **read** outer function variables
- ✅ Use `global` to modify global variables
- ✅ Use `nonlocal` to modify outer function variables
- ✅ Without these keywords, assignment creates a new local variable

**Examples:**
- Modifying global variables from within functions
- Accessing outer function variables in nested functions
- Using `nonlocal` to modify enclosing scope variables
- Deeply nested function hierarchies

---

### 4. 💡 Type Hints & Input Validation (`tips.ipynb`)

**Topics Covered:**
- Type hints and function annotations
- Type checking with `isinstance()`
- Input validation patterns
- Writing clear function documentation

**Key Concepts:**
- **Type Hints:**
  - Provide documentation and IDE support
  - Use syntax: `def function(param: type) -> return_type:`
  - **Do NOT enforce runtime type checking**

- **Input Validation:**
  - Always validate inputs if type safety is important
  - Use `isinstance()` instead of `type()` for type checking
  - Provide clear error messages when validation fails

**Best Practices:**
- Use type hints for better code documentation
- Validate inputs in critical functions
- Write clear docstrings explaining function behavior
- Handle type errors gracefully with informative messages

**Examples:**
- Functions without type hints
- Adding type annotations
- Manual type checking with `type()`
- Using `isinstance()` for type validation
- Writing comprehensive docstrings

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Jupyter Notebook or JupyterLab

### Running the Notebooks

1. **Install Jupyter** (if not already installed):
   ```bash
   pip install jupyter
   ```

2. **Start Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

3. **Open any notebook** from the file browser and run the cells

### File Dependencies

Some notebooks use external files:
- `users.txt` - Used in `fileOperations.ipynb`
- `students.txt` - Created/modified in `fileOperations.ipynb`
- `mycv.txt` - Created/modified in `fileOperations.ipynb`

---

## 📖 Learning Path

Recommended order for studying:

1. **Start with**: `errors_exceptions.ipynb` - Learn how to handle errors
2. **Then**: `fileOperations.ipynb` - Understand file I/O operations
3. **Next**: `scoping.ipynb` - Master variable scoping concepts
4. **Finally**: `tips.ipynb` - Learn type hints and validation

---

## 🎯 Learning Objectives

After completing these notebooks, you will be able to:

- ✅ Handle exceptions and errors gracefully in Python
- ✅ Read, write, and append data to files
- ✅ Understand and work with different variable scopes
- ✅ Use type hints and validate function inputs
- ✅ Write clean, maintainable Python code following best practices

---

## 📝 Notes

- All notebooks include practical examples with outputs
- Code cells can be executed interactively
- Markdown cells provide explanations and context
- Examples progress from simple to more complex concepts

---

## 🤝 Contributing

This is an educational repository. Feel free to:
- Add more examples
- Improve explanations
- Fix any errors
- Suggest additional topics

---

## 📄 License

This educational content is provided for learning purposes.

---

## 🔗 Related Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)
- [Python Exception Handling](https://docs.python.org/3/tutorial/errors.html)
- [Python File I/O](https://docs.python.org/3/tutorial/inputoutput.html)

---

**Happy Learning! 🎓**

