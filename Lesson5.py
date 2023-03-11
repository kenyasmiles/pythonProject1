#dictionary
car={
    "brand":"subaru",
    "model":"impreza",
    "YOM":1964
}
print(car)
#type
print(type(car))
#printing the values
print(car.values())

#print the keys
print(car.keys())

#change the values in dictionary
car["brand"]="bmw"
print(car.values())

#add another pair/item
car["color"]="blue"
print(car)

#create a key whose value is a list
car["CC"]=[1200,1300,1500,2000]
print(car)

car.pop("brand")
print(car)

new={
    "mileage":"50,000km",
    "seat memory":"button1",
    "seat capacity":5
}
car.update(new)
print(car)