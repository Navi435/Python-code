1.#Create a Dictionary with at least 5 key value pairs of the Student ID and Name 
students = {
    201: "Navi",
    202: "Keer",
    203: "Jyo",
    204: "Sri",
    205: "Priya"
}
print(students)

1.1#Adding the values in dictionary 
students[206]='Asmi'

print(students)

1.2#Updating the values in dictionary 
students[201]="Naveena"
print(students)

1.3#Accessing the value in dictionary 
print(students[205])

1.4#Create a nested loop dictionary 
students2 = {
    201: {"name": "Sri", "age": 20, "marks": 80},
    202: {"name": "Keer", "age": 19, "marks": 90},
    203: {"name": "Jyo", "age": 21, "marks": 70},
}

print("Nested Dictionary:",students)

1.5#Access the values of nested loop dictionary 
print("201:",students2[201])

1.6#Print the keys present in a particular dictionary 
print("keys :",students.keys())

1.7#Delete a value from a dictionary 
del students[203]

print(students)
