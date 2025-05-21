# Dictionary
# A dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

dict = {
    "brand" : "Tasla",
    "model" : "Model S",
    "year" : 2020,
}

dict["brand"] = "Toyata"
dict["color"] = "red"
print(dict.keys())


# Dictionary Methods
# keys()
 
#  nested dictionary

student = {
    "name": "Ali",
    "age": 20,
    "subjects" : {
        "math": 90,
        "english": 85,
        "science": 95,
        "computer": 100
    }
}
print(student["subjects"]["math"]) 
# update

student.update({"name": "Ahmed"})
print(student)