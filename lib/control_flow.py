#!/usr/bin/env python3

# Question 1
def admin_login(username, password):
    # your code here
    pass
    if (username == "admin" or username == "ADMIN") and password == "12345" :
        return "Access granted"
    else:
        return "Access denied"

admin_login("sudo", "12345")
print(admin_login("sudo", "12345"))

admin_login("admin", "12345")
print(admin_login("admin", "12345"))

admin_login("ADMIN", "12345")
print(admin_login("ADMIN", "12345"))

#Question 2
def hows_the_weather(temperature):
    # your code here
    pass
    if temperature > 85:
        return "It's too dang hot out there!"
    elif temperature >= 40 and temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature < 40:
        return "It's brisk out there!"
    else:
        return "It's perfect out there!"

hows_the_weather(33)
print(hows_the_weather(33))

hows_the_weather(99)
print(hows_the_weather(99))

hows_the_weather(75)
print(hows_the_weather(75))


def fizzbuzz(num):
    # your code here
    pass
    if (num % 5 == 0 and num % 3 == 0):
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    else:
        return num

fizzbuzz(1)
print(fizzbuzz(1))

fizzbuzz(2)
print(fizzbuzz(2))

fizzbuzz(3)
print(fizzbuzz(3))

fizzbuzz(4)
print(fizzbuzz(4))

fizzbuzz(5)
print(fizzbuzz(5))

fizzbuzz(15)
print(fizzbuzz(15))

def calculator(operation, num1, num2):
    # your code here
    pass
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None

calculator("+", 1, 1)
print(calculator("+", 1, 1))

calculator("-", 3, 1)
print(calculator("-", 3, 1))

calculator("*", 3, 2)
print(calculator("*", 3, 2))

calculator("/", 4, 2)
print(calculator("/", 4, 2))

calculator("nope", 4, 2)
# print(calculator("nope", 4, 2))

