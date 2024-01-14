fruitsList = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

# add item at position
fruitsList[1:3] = ["blackcurrant", "watermelon"]


# insert at position 2
fruitsList.insert(2, "watermelon") 

# To add an item to the end of the list, use the append() method:
fruitsList.append("Lucy")

# extend another list 
tropical = ["mango", "pineapple", "papaya"]
fruitsList.extend(tropical)

#remove specified item
fruitsList.remove("mango") 
fruitsList.remove("mango") 

# remove last item using pop()
fruitsList.pop()
fruitsList.pop(3)

#  delete list completely
carList = ["bmw", "jpe", "honda"]


print("deleting carlist ")
# del carList 
carList.clear()
# print(fruitsList )
# print(carList)  #carlist is not defined

# For loop
for x in fruitsList:
    print(x) #loop through a list

print("break............")
i = 0
while i < len(fruitsList):
  print(fruitsList[i])
  i = i + 1

print("break............")

[print(x) for x in fruitsList] #short hand 