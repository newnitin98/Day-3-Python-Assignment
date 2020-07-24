# Day 3 Assignment 2 Take a Interger and find number is prime or not
# taking input from user
number = int(input("Enter any number: "))

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

# if the entered number is less than or equal to 1
else:
    print(number, "is not a prime number")