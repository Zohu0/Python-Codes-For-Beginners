def percentfunc(mark):
    p= ((mark[0] + mark[1] + mark[2] + mark[3] + mark[4])/500)*100
    return p

a= [56,67,98,87,76]
percentage1= percentfunc(a)

b= [68,78,54,96,75]
percentage2= percentfunc(b)
print(percentage1, percentage2)