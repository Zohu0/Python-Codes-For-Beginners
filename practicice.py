
f= open("open.txt", "r")
t= f.read()


if "twinkle" in t:
    print("Twinkle Is Present")
else:
    print("Twinkle Is Not Present")

f.close()