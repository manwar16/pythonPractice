#List Declaration
grocery_list = ["Rice", "Potato", "Tomato"]
print(grocery_list)

print(grocery_list[1])

l2 = list()
print(l2)



#Added an item in list
grocery_list.append("Water")
print(grocery_list)

l2.append(4)
print(l2)

l2.append("computer")
print(l2)

#changing item
l2[1]='Mango'
print(l2)

grocery_list[2]='Banana'
print(grocery_list)

grocery_list.insert(1, "orange")
print(grocery_list)

#Remove any specified item
grocery_list.remove("orange")
print(grocery_list)

#Remove Last item in the list
grocery_list.pop()
print(grocery_list)

#Join Tow list
joinList= grocery_list + l2
print(joinList)

grocery_list.extend(l2)
print(grocery_list)





