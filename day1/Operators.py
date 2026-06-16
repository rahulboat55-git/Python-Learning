# Operators -> Operators in Python are symbols used to perform operations on variables and values.
# 1. -> 1. Arithmetic Operators -> +, -, *, /, //, ** etc..

# program
# a = 2
# b = 4
# add = a+b
# sub = a-b
# mul = a*b
# div = b/a
# flordiv = b//a
# doublemul = a**b
# print(add) 
# print(sub)
# print(mul)
# print(div)
# print(flordiv)
# print(doublemul)

# que1. -> Write a program to take two numbers as user input and perfom all the arthmatic
# # on opeerations on that input
# a = int(input("enter a number"))
# b = int(input("enter b number"))
# # performing addition
# add = a+b
# print(add)

# # performing sub
# sub = a-b
# print(sub)

# # performing multi
# mul = a*b
# print(mul)

# # performing divison
# div = a/b
# print(div)

# # performing flordivison
# flordiv = a//b
# print(flordiv)

# # performing power
# power = a**b
# print(power)



# 2.Assignment Operator -> assign values
# -> =, +=, -=, *=, /= 

# a = 10
# b = 20
# # print(" Before adding", a)
# # c = a+b
# # a = c
# # print("after adding", a)

# # +=
# a += b
# print(a)

# #-=
# a -= b
# print(b)

# # *=
# a *= b
# print(a)

# # /=
# a /= b
# print(a)

# # //=
# a //= b
# print(a)


# 3. Comparison Operrators -> ==, !=, <, >, <=, >=

# a = 10
# b = 10
# print(a==b)      # equal to (==)
# print(a!=b)      # not equal to (!=)
# print(a>b)       # grater tham (>)
# print(a<b)       # smllar tham (<)
# print(a<=b)      # smalle and equal to (<=)
# print(a>=b)      # grater and equal to (>=)


# 4.Logical Operators -> Logical operators are used to combine or modify conditions.
# 1. and Operator ->Returns True only if both conditions are True
# 2. or Operator -> Returns True if at least one condition is True.
# 3. not Operator -> Reverses the result

# a = 10
# b = 20
# c = 30

# # or operators
# print(a<b or b<c)   
# print(a<b or a>b)
# print(a>b or a>b)

# # and operators
# print(a<b and b<c)   
# print(a<b and a>b)
# print(a>b and a>b)

# # not operators
# print(not(a > b))
# print(not(a < b))



# Bitwisw Operators -> Bitwise operators work on the binary (bit) representation of numbers.

# 1. Bitwise AND (&)-> Returns 1 only if both bits are 1
# a = 5   # 0101
# b = 3   # 0011
# print(a & b)

# # 2. Bitwise OR (|) -> Returns 1 if at least one bit is 1
# print(5 | 3)

# # 3. Bitwise XOR (^) -> Returns 1 if the bits are different
# print(5 ^ 3)

# # 4. Bitwise NOT (~) -> Inverts all bits.
# print(~5)

# # 5. Left Shift (<<) -> Shifts bits to the left by the specified number of positions
# print(5 << 1)

# # 6. Right Shift (>>) -> Shifts bits to the right.
# print(5 >> 1)


# 6. Membership Operators -> Membership operators are used to check whether a value exists in a 
# sequence such as a string, list, tuple, set, or dictionary.

# There are two membership operators
# 1. in Operator -> Checks if a value exists in a sequence
# name = "Python"
# print("P" in name)

# numbers = [10, 20, 30, 40]
# print(20 in numbers)

# # 2. not in Operator -> Checks if a value does not exist in a sequence.
# name = "Python"
# print("z" not in name)

# numbers = [10, 20, 30, 40]
# print(50 not in numbers)



# 7. Identity Operators -> Identity operators are used to check whether two variables refer to the same object in memory.

# There are two identity operators:

# is Operator ->	Returns True if both variables point to the same object
a = [1, 2, 3]
b = a
print(id(a))
print(id(b))
print(a is b)
# is not Operator ->	Returns True if both variables point to different objects
a = [1, 2, 3]
b = [1, 2, 3]

print(a is not b)





##  Operator Precedence in Python -> Operator precedence determines the order in which operators are evaluated in an expression.

