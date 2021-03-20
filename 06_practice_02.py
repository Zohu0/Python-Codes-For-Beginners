sub1= int(input("Enter Your First Subject Marks: "))
sub2= int(input("Enter Your Second Subject Marks: "))
sub3= int(input("Enter Your Third Subject Marks: "))

if(sub1<33 or sub2<33 or sub3<33):
    print("You Are Fail")
elif(sub1+sub2+sub3)/3 <40:
    print("You Are Fail Due To The Less Percentage")
else:
    print("You Are Pass")