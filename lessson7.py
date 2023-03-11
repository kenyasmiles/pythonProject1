#if statements
#awarding students grades based on their performance
#use input  function to let the user input their ouwn values
marks=int(input("Enter Marks:"))# declaration of the data type
if marks >=0 and marks <50:
    print(marks,"your grade is E")
elif marks >=50 and marks <60:
    print(marks,"your grade is D")
elif marks >=60 and marks <70:
    print(marks,"your grade id C")
elif marks >=70 and marks <80:
    print(marks,"your grade is B")
elif marks >=80 and marks <=100:
    print(marks,"congratulations ,your grade is A")
else:
    print(marks,"invalid marks")

#nested if
#check whether students qualifies to move to the next class
#someone can move to the next class only when they have 80 and above ,18+
age =int(input("Enter Age of Student:"))
english =str(input("enter the grade"))
name =str(input("Enter name of student:"))
if marks >=80 and marks <=100:
    if age >=18:
        if english =="B":
            print("You qualify for first exam")
        print(name,age,"qualify for university")
    else:
        print("you passed but under age")

else:
    print("you dont qualify")


