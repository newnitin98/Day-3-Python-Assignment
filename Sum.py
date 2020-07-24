# Day 3 Assignment 1 Sum of n number using while loop
n = int (input("Enter the number "))
sum1 = 0
i = 1
while i<=n:
    sum1 = sum1 + i
    i = i + 1 
    print(sum1)
print (f"sum of n number is: {sum1}")