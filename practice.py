with open("sample.txt", "r") as f:
    content= f.read()

content= content.replace("donkey", "****")

with open("sample.txt", "w") as f:
    content= f.write(str(content))