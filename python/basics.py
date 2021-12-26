# Basics
# Datatypes
# DocStrings
# Strign Interpolation
# Arithmetic
# Operator Precedence
# Booleans
# Operators

print("Hello World !")

# Datatypes

# Some built in data types
#
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview

# it is a dynamic typed language
x = 5
print(type(x))
x = "Prince"
print(type(x))

# Docstrings
# usually to indicate documentation
    """Set the code below

    Just a little something
    and this docstring part is treated as a comment
    BTW you can also use print to print this
    """
# can have following
# param and type    : Parameter and its variable type
# return and rtype  : Specify both the return value and type of the function or method
# .. seealso        ::: Further reading
# .. notes          ::: Add a note
# .. warning        ::: Add a warning

# Simple String interpolation
variable = "Prince"
print("I am " + variable)
intVariable = 12
# print("This is an integer variable" + intVariable)
# ERROR : can't concatenate numbers with strings
print("The int variable value is %s" % (intVariable))

# f-strings
# PEP 498 introduced a new string formatting mechanism known as Literal String Interpolation or more commonly as F-strings
print(f"Hi I am {variable} and my Integer value is : {intVariable}")


# Arithmetic Operator can work on strings too , let's see
# +
int1 = 12
int2 = 14
string1 = "Prince"
string2 = "Programmer"


print(int1 + int2) # 26
# print(string1 + int2) # TypeError: can only concatenate str (not "int") to str
print(string1 + string2) # PrinceProgrammer

# -
print(int2 - int1)
# print(string1 - string2) TypeError: unsupported operand type(s) for -: 'str' and 'str'

# *
print(int2 * 5)
print(string1 * int1)
# print(string1 * string2) TypeError: can't multiply sequence by non-int of type 'str'

# /
print(int1 / 3)
# print(string1 / int1) TypeError: unsupported operand type(s) for /: 'str' and 'int'
# print(string2 / string1) TypeError: unsupported operand type(s) for /: 'str' and 'str'

# %

print(int1 % 5)
# print(string1 % 2) TypeError: not all arguments converted during string formatting
# print(string2 % string1) TypeError: not all arguments converted during string formatting

# //
print(int1 // 7) # gives out the quotient for numeric division


# **
print(3 ** 3) # exponent operator

# Operator Precedence in Decreasing Order
# () > ** > +x, -x, ~x > *, /, //, % > +, - > <<, >> > & > ^ > | > ==, !=, >, >=, <, <=, is, is not, in, not in , not , and , or
# Useful in mathematical operations , Kind of like Bodmas Rule


# Booleans
truevar = True
falsevar = False
# also postive or negative integars other than 0 are True , 0 is False
x = 9
if(x):
    print("True")

# Logical Operators
# > , < , >= , <=, !=

# >
# print(int2 > int1)
# print(string1 > int2) TypeError: '>' not supported between instances of 'str' and 'int'
# print(string1 > string2)

# Kind of same for many of them..

# is : The “is keyword” is used to test whether two variables belong to the same object.
x = 10
y = 10
z = '10'
print(x is y) # True as value is same and so is type
print(x is z)

# if x is y:
#     print(True)
# else:
#     print(False)
