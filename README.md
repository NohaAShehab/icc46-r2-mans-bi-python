# 📚 Day 01 - Python Fundamentals

Welcome to Day 01 of the Python course! This directory contains comprehensive notebooks covering fundamental Python concepts.

---

## 📖 Notebooks Overview

This directory includes two main educational notebooks:

### 1. 🔤 `string-ops.ipynb` - String Operations

A comprehensive guide to working with strings in Python, covering everything from basic operations to advanced formatting techniques.

### 2. 🐍 `variables_types.ipynb` - Variables and Types

An in-depth exploration of Python variables, data types, type conversion, and conditional logic.

---

## 📋 Table of Contents

- [String Operations Notebook](#-string-opsipynb)
- [Variables and Types Notebook](#-variables_typesipynb)
- [Key Concepts](#-key-concepts)
- [Getting Started](#-getting-started)

---

## 🔤 `string-ops.ipynb`

### Topics Covered

#### 🔒 String Immutability
- Understanding that strings are immutable in Python
- How operations create new strings rather than modifying existing ones

#### 🔪 String Slicing
- **Basic Slicing**: `string[start:end]` syntax
- **Step Values**: Using `[start:end:step]` for advanced slicing
- **Reversing Strings**: Using negative step values `[::-1]`
- **Indexing**: Zero-based indexing and accessing characters

#### 🔍 String Methods
- **Finding Information**:
  - `len()` - Get string length
  - `count()` - Count character occurrences
  - `index()` - Find character position
- **Case Conversion**:
  - `capitalize()` - First character uppercase
  - `title()` - Title case
  - `upper()` - All uppercase
  - `lower()` - All lowercase

#### 🎨 String Formatting
- **Concatenation**: Using `+` operator
- **String Repetition**: Using `*` operator
- **`.format()` Method**: Positional and named placeholders
- **F-Strings**: Modern f-string formatting (Python 3.6+)

#### 🔄 String Replacement
- Manual replacement using loops
- Using `.replace()` method
- Limiting replacements with count parameter

#### ⌨️ User Input
- Understanding `input()` always returns strings
- Type conversion for user input
- Common mistakes with string concatenation vs addition

#### ✅ String Validation
- `isdigit()` - Check if all characters are digits
- `isspace()` - Check if all characters are whitespace
- `isascii()` - Check if all characters are ASCII

#### ✂️ String Stripping
- `rstrip()` - Remove from right
- `lstrip()` - Remove from left
- `strip()` - Remove from both ends
- Custom character stripping

#### 🔍 The `in` Operator
- Checking if characters/substrings exist in strings
- Boolean return values

---

## 🐍 `variables_types.ipynb`

### Topics Covered

#### 🔄 Type Conversion
- **Conversion Functions**:
  - `int()` - Convert to integer
  - `float()` - Convert to float
  - `str()` - Convert to string
  - `bool()` - Convert to boolean
- **Valid vs Invalid Conversions**: Understanding when conversions work and when they raise errors
- **Integer to Float**: Converting between numeric types

#### ⚖️ Comparison Operators
- `==` - Equal to
- `!=` - Not equal to
- `>` - Greater than
- `<` - Less than
- `>=` - Greater than or equal
- `<=` - Less than or equal
- **Special Cases**: Boolean and integer comparison (`True == 1`)
- **Type Mismatches**: String vs integer comparisons

#### 🔀 Logical Operators
- **`and` Operator**: Returns first falsy value or last value if all truthy
- **`or` Operator**: Returns first truthy value or last value if all falsy
- **`not` Operator**: Returns opposite boolean value
- **Special Behavior**: Logical operators don't always return `True`/`False`

#### ✅ Truthiness in Python
- **Truthy Values**: Non-empty strings, non-zero numbers, non-empty collections, `True`
- **Falsy Values**: Empty strings `""`, `0`, `0.0`, `None`, empty collections `[]`, `{}`
- **Using Truthiness**: Direct use in `if` statements

#### 🔄 Boolean Conversion
- Using `bool()` function
- Understanding what values convert to `True` or `False`

#### 🎯 Conditional Statements
- **If-Elif-Else Structure**: Checking multiple conditions
- **Key Points**:
  - Only first matching condition executes
  - Once a condition is met, rest are skipped
  - `else` is optional

---

## 🎯 Key Concepts

### String Immutability
> **Important**: Strings in Python are immutable. Any operation on a string creates a new string object rather than modifying the original.

### Type Conversion
> **Note**: Not all type conversions are possible. Converting incompatible types will raise `ValueError` or `TypeError`.

### Truthiness
> **Key Concept**: Python evaluates values as "truthy" or "falsy" in boolean contexts, allowing direct use in conditionals without explicit comparison.

### Logical Operators
> **Special Behavior**: Logical operators (`and`, `or`) return the last evaluated value, not always `True` or `False`.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher (for f-string support)
- Jupyter Notebook or JupyterLab

### Running the Notebooks

1. **Open Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

2. **Navigate to the directory**:
   ```bash
   cd day01
   ```

3. **Open the notebooks**:
   - Click on `string-ops.ipynb` or `variables_types.ipynb`
   - Run cells sequentially using `Shift + Enter`

### Recommended Learning Path

1. **Start with** `variables_types.ipynb` to understand:
   - Basic data types
   - Type conversion
   - Comparison and logical operators
   - Conditional statements

2. **Then explore** `string-ops.ipynb` to learn:
   - String manipulation
   - String methods
   - String formatting
   - User input handling

---

## 💡 Tips for Learning

- **Run the code**: Don't just read - execute the cells and see the output
- **Experiment**: Try modifying the examples to see what happens
- **Practice**: Create your own examples based on the concepts
- **Read the markdown**: The notebooks include detailed explanations and examples

---

## 📝 Example Code Snippets

### String Formatting
```python
# Using .format()
template = "Hello {name}, you are {age} years old"
message = template.format(name="Alice", age=25)

# Using f-strings (preferred)
name = "Alice"
age = 25
message = f"Hello {name}, you are {age} years old"
```

### Type Conversion
```python
# String to integer
num_str = "42"
num_int = int(num_str)  # 42

# Integer to float
num_int = 42
num_float = float(num_int)  # 42.0
```

### Truthiness
```python
# Using truthiness in conditionals
name = "Alice"
if name:  # True (non-empty string is truthy)
    print("Name exists")

empty_name = ""
if empty_name:  # False (empty string is falsy)
    print("This won't print")
```

---

## 🎨 Notebook Features

Both notebooks include:
- ✨ **Colorful styling** for better readability
- 📚 **Detailed explanations** with examples
- 💡 **Tips and warnings** for common mistakes
- 🔍 **Code examples** with syntax highlighting
- 📊 **Visual tables** for quick reference
- ⚠️ **Error examples** to learn from mistakes

---

## 📚 Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Python Built-in Functions](https://docs.python.org/3/library/functions.html)

---

## 🤝 Contributing

If you find any errors or have suggestions for improvement, please feel free to contribute!

---

## 📄 License

This educational material is provided for learning purposes for BI Students at ITI .

---

## 👤 Author

**Noha Shehab**  
📧 Email: [nshehab@iti.gov.eg](mailto:nshehab@iti.gov.eg)

---

**Happy Learning! 🎉**

