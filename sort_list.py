thislist = [100, 50, 65, 82, 23]

thislist.sort()
print(thislist)

thislist.sort(reverse = True)
print(thislist)


# The function will return a number that will be used to sort the list (the lowest number first):
def myfunc(n):
  return abs(n - 50)

numList = [100, 50, 65, 82, -10, 23]

numList.sort(key = myfunc)
numList.reverse() #reverse the sort

mylist1 = numList.copy()
mylist2 = list(numList)
print(numList,"br--", mylist1, "break", mylist2)
