#TASK 1
#Creating a list which inculde Top Company names 
my_list = [ 18,45,12,100 ]
print("Initial List:", my_list)

#Adding an element to the list
my_list.append(22)
print("New List after addition of an Element:", my_list)

#Remove an element fron the list
my_list.remove(100)
print("New List after Removing an Element:", my_list)

#Modifiying An Elemet in the list
my_list[2] = 101
print("New List after Modifiying an Element:", my_list)

print(" Updated List :", my_list)


#TASK 2
#Creation a Dictionary
my_dict = { 'Product' : 'Motorola', 'Model' : ' Edge 50 Fusion', 'Launch' : '22 May'}
print("Initial Dictionary:", my_dict)

#Adding an Element in the Dictionary
my_dict['Processor' ] = 'Snapdragon'
print("\nNew Dictionary after addition of an Element:", my_dict)

#Removing an Element in the  Dictionary
del my_dict['Launch']
print("\nNew Dictionary after Removing an Element:", my_dict)

#Modifiying an Element in the Dictionary
my_dict ['Model'] = 'Edge 50 Pro'
print("\nNew Dictionary after Modifiying an Element:", my_dict)

print("\nUpdated Dictionary :", my_dict)


#TASK 3
#Creating a Set 
my_set = { 2,7,12,29,}
print("Initial Set:", my_set)

##Adding an Element in the Set
my_set.add(17)
print("\nNew Set after addition of an Element:", my_set)

#Removing an Element in the  Set
my_set.remove(7)
print("\nNew Set after Removing an Element:", my_set)

#Modifiying an Element in the Set
my_set.discard(12)
my_set.add(21)
print("\nNew Set after Modifiying an Element:", my_set)

print("\nUpdated Set :", my_set)



