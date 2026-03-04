# today i joined late, so i will write the code for the previous class, which is about (06-list,07-tuples,08-sets,09-dictionaries) from the pdf.
# 06-list
# fruits = ["apple", "banana", "orange"]
# numbers = [1,2,3,4,5]
# mixed = ["hello", 42, 3.14, True]
# empty_list = []

# fruits.append("grape") #add an element to the end of the list
# fruits.insert(1, "kiwi") #add an element at a specific index
# fruits.remove("banana") #remove an element by value
# popped = fruits.pop() #remove and return the last element of the list
# fruits.sort() #sort the list in ascending order
# fruits.reverse() #reverse the order of the list


# print(fruits[1]) #accessing list element; index starts at 0, so fruits[1] is "banana"
# print(fruits[-1]) #accessing last element of the list, which is "orange"
# print(numbers[1:4]) #slicing the list, which gives us [2,3,4]
# print(numbers[:3]) #slicing from the beginning to index 3 (exclusive), which gives us [1,2,3]
# print(numbers[2:]) #slicing from index 2 to the end, which gives us [3,4,5]

# # 06-list operation: CRUD a list

# #list operations
# len(fruits) #get the length of the list
# "apple" in fruits #check membership in the list, returns True if "apple" is in fruits

# JUMP TO WHERE THE CLASS IS CURRRENTLY AT, WHICH IS 09-dictionaries
# 09-dictionaries

# student = {
#     "name": "Firdaus",
#     "age": 39,
#     "grade": "A",
#     "courses": ["Python", "LINUX", "micro python"]
# }

# # Accessing and modifying

# student["grade"] = "C"  # Update grade
# student["study method"] = "online bootcamp- jomhack" # Add new key-value pair

# print(student["name"])  # Output: Firdaus
# print(student.get("courses")) # Output: ['Python', 'LINUX', 'micro python']
# print(student.get("study method")) # Output: online bootcamp- jomhack

# keys = student.keys()
# values = student.values()

# print(keys)
# print(values)
# print(student.items())


# # Iterating through the dictionary
# for key in student:
#     print(f"{key}: {student[key]}")

# # this is the same as:
# for key, value in student.items():
#     print(f"{key}: {value}")

STE = {
    "JOB": {
        "KLCC": {"done": 70, "pending": 30},
        "Hijauan Kemensah": {"done": 60, "pending": 40}
    },
    "TOOLS": ["DRILL", "HAMMER", "SCREWDRIVER"]

}
# nested dictionary access is done by chaining keys together so to access the "done" value for KLCC, we can use:
print(STE["JOB"]["KLCC"]["pending"]) # Output: 30
# print(STE["TOOLS"]) # Output: ['DRILL', 'HAMMER', 'SCREWDRIVER']