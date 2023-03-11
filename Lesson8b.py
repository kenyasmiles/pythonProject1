#python  functions
#  is a block of code that is executed only when called
# and performs a specific task
#use keyword def to create python functions
# syntax def name ():
#when calling the function use the name of the function and parenthesis
#wehave user defined function and built in functions
#built-in sum(),print(),type,len()

numbers=(15,35,24,4,56,67)
addition=sum(numbers)
print(addition)
print(type(addition))

def name():
    name=("brian")
    print(name)
name()
def calc():
    num1=70
    num2=21
    addition=num1+num2
    print(addition)
calc()
def personal_details():
    name =("brian")
    age=25
    status="single"
    id=34236562
    kra="P213231641"
    print(f"{name} who is {age} years old and"
            f"ID Number {id},kra pin {kra} is {status}")
personal_details()
