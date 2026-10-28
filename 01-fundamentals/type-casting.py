# Type or Typecasting
# Type casting means converting one data type into another.
# Python supports built-in type conversion functions like int(), float(), str(), bool().

# Examples:
num_str = "123"
num_int = int(num_str)
print(num_int)         # 123
print(type(num_int))   # <class 'int'>

price = 49.99
price_int = int(price)
print(price_int)       # 49

value = 5
print(float(value))   # 5.0
print(str(value))     # "5"
print(bool(value))     # True

# Notes:
# - int("123") -> 123
# - float("3.14") -> 3.14
# - str(45) -> "45"
# - bool(0) -> False
# - bool(1) -> True
# - Converting a float to int removes the decimal part.
