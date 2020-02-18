y=input("Enter current year ")
y=int(y)
x=input("Enter your year of birth ")
x=int(x)
age=y-x
age=int(age)
if age<0:
    print("Error, please check your input again")
elif(age>=2 and age<4):
    print("Toodler")
elif(age>=4 and age<10):
    print("Preschool age")
elif(age>=10 and age<14):
    print("Gradeschool age")
elif(age>=14 and age<17):
    print("High School year")
elif(age>=17 and age<20):
    print("College year")
elif(age>=20 and age<65):
    print("Adult")
elif age>150:
    print("You're dead, your bone are left")
else:
    print("Old age")
