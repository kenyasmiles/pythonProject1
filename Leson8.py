#while loop
# the body inside while is executed as long as the condition is satisfied
#whilw the condition is true ,the loop continues
# we exit the loop when the condition is not true
# make sure you increament the value you are testing
count =1
while count <6:
    print(count,"Print the value of count")
    #increament
    count=count +1

patients =1
while patients <10:
    Name =input("Enter the patients name:")
    weight = int(input("Enter your Weight;"))
    height = float(input("Enter our Height"))
    BMI = weight / height ** 2  # exponentiation
    print("the body mass index of person X", BMI)

    if BMI < 18.5:
        print(BMI,patients, "Underweight")
    elif BMI >= 18.5 and BMI <= 22.9:
        print(BMI,patients, "Normal")
    elif BMI >= 23 and BMI <= 24.9:
        print(BMI,patients, "Overweight")
    elif BMI > 25 and BMI <= 29.9:
        print(BMI,patients, "Pre Obese")
    elif BMI > 30 and BMI <= 34.9:
        print(BMI,patients, "obese class 1")
    elif BMI > 35 and BMI <= 39.9:
        print(BMI,patients, "Obese class 2")
    elif BMI >= 40:
        print(BMI,patients, "obese class 3")
        patients=patients+1
    if patients==2:
        print("enough patients")
        break


