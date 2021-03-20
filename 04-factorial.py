# n=4
# factorial= 1

# for i in range(n):
#     factorial=factorial*(i+1)
# print(factorial) 

def factorial():
    product=1
    
    for i in range(n):
        product= product* (i+1)
    return product

n=int(input("Enter no: ")) 
f= factorial()
print(f)