# Program to print multiplication table of n using for loop in reversed order
n = int(input("Enter a number: "))

for i in range(10, 0, -1):
    print(f"{n} x {i} = {n * i}")

