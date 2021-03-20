f= open('sample.txt', 'r')
data=f.read()
# data=f.read(8) # read the Eight five character of file
print(data)
f.close()