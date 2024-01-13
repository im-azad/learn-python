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

print(fruitsList)