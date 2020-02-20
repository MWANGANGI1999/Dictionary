#colllection which is unordered
#changable and indexed
student={
         "name" : "James",
         "email" : "james@gmail.com",
         "phone_no" :"0700222222",
}
print(student)

#accessing items
x=student['email']
print(x)
print(student['name'])
#get() Returns the value of the specified key
y=student.get('email')
print(y)

#change values
student['name']='john'
print(student)

#loop through dictionary
#prints all key names in the dictionary
for s in student:
    print(s)

#values() Returns a list of all the values in the dictionary
for value in student.values():
    print(value)

#Accessing items
#items()Returns a list containing a tuple for each key value pair
#it displays all the keys and values in the dictionary.
for k,v in student.items():
    print(k,v)

#check if item exists
#if an item exists then its displays that the item is there
if "name" in student:
    print('name is there')
else:
    print('name is not there')
#if an item exists then its displays that the item is there
if "birthday" not in student:
    print('birthday is not there')
else:
    print('birthday is there')
if "location" in student:
    print('location is there')
else:
    print('location is not there')
if "status" not in student:
    print('status is not there')
else:
    print('status is there')

#adding an item
#it add the student registration number to the student information
student['reg_no']="BSCIT-01-0687/2019"
print(student)
#it add the Guardian name to the student information
student['Guardian']="Mwangangi"
print(student)
#it add the guardian number to the student information
student['Guardian_no']="0700200120"
print(student)

#remove an item
#it removes/delete an item from the dictionary
student.pop('location')
print(student)
#removes the item with the specified key name
del student["Guardian"]
print(student)
#The popitem() method removes the last inserted item 
student.popitem()
print(student)
#update() Updates the dictionary with the specified key-value pairs
student.update({"email": "john@gmail.com"})
print(student)
#The copy() method returns a copy of the specified dictionary.
x = student.copy()
print(x)
#The keys() method returns a view object. The view object contains the keys of the dictionary, as a list
x = student.keys()
print(x)
#The clear() method removes all the elements from a dictionary
student.clear()
print(student)
