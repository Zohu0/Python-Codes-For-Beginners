num= int(input("Enter Any Number: "))

factorial= 1
for i in range(1, num+1):
    factorial= factorial*i
print(f"The Factorial Of {num} Is {factorial}")