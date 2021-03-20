num= int(input("Enter Ant Number "))
prime= True 

for i in range(2,num):
    if(num%i==0):
        prime= False
        break
if prime:
    print("This Is Prime Number")
    
else:
    print("This Is Not Prime Number")

