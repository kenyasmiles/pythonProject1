#for loop
courses=["Web Development","Data Science","Cyber Security","Mobile development"]
print(courses)
for course in courses:
    print(course)
emails=["max@gmail.com","lewis@gamil.com","shan@gmail.com","brian@gmail.com","class@gmail.com","trial@gmail.com"]
#print(len(courses))
#for email in emails:
    #if email =="max@gmail.com":
      #  print("no need to send him an email")
    #    break
   # print(email)
print(len(courses))
for email in emails:
    if email ==emails[3]:
        print("enough persons")
        print(("end of example"))
        break
        #anything statement or code after break is not executed
    print(email)

#continue
#ignores the current item but continues with the loop
for email in emails:
    if email == emails[3]:
        continue
    print(email)