import csv

user_id = input("Enter user id to search: ")

with open("practice.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        if row[0] == user_id:          
            print("Password:", row[1])  
            break
    else:
        print("User not found.")
