#counting down with loops
start_num = int(input("What is your starting number?"))
while start_num != 0:
    print(start_num)
    start_num = start_num-1
print("Blast off! 🚀")

#mult table with for loops
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num*i)
    
#find factorial
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print("The factorial of", num, "is", factorial)

