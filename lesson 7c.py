#recap on if statements
#BMI PROGRAMM
weight=int(input("Enter your Weight;"))
height=float(input("Enter our Height"))
BMI=weight/height**2 #exponentiation
print("the body mass index of person X",BMI)

if BMI <18.5 :
    print(BMI,"Underweight")
elif BMI >=18.5 and BMI <=22.9:
    print(BMI,"Normal")
elif BMI >=23 and BMI <=24.9:
    print(BMI,"Overweight")
elif BMI >25 and BMI <=29.9:
    print(BMI,"Pre Obese")
elif BMI >30 and BMI <=34.9:
    print(BMI,"obese class 1")
elif BMI >35 and BMI <=39.9:
    print(BMI,"Obese class 2")
elif BMI >=40:
    print(BMI,"obese class 3")