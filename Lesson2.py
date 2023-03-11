#python lists
#list is one of the data types
#it is defibned with square brackets {}
#list is ordered,changeable,allows duplicates
customers=["Brian","lewis","Maxwell"]
print(customers)

#access individual items
print(customers[0])
#negative indexing
print(customers[-1])

#change
customers[0]="JOSEPH"
print(customers)

#add append
customers.append("Brian")
print(customers)

#remove/pop
customers.pop(2)
print(customers)

#add more than one item to the list
new=["dan","ben","Erick"]
customers.extend(new)
print(customers)

#delete customers
del customers







