import os
if not os.path.exists("merge.txt"):
    with open("merge.txt", "wb") as f:       
        f.write(b"Python programming is fun to learn! This file is used for file handling demo.")
f = open("merge.txt", "rb")
print("Print the initial position:", f.tell())
print("Move the cursor to 4th position:", f.seek(4, 0))
print("Display next 5 characters:", f.read(5))
print("move the cursor to the next 10characters",f.seek(10, 1))
print("Print the current position:", f.tell())
print("Move the cursor to 4th position again:", f.seek(4, 0))
print("Display next 5 characters:", f.read(5))

print("Move the cursor 10 bytes forward from current position:", f.tell())
print("The current cursor position:", f.tell())
print("Print next 10 characters from the current cursor position:", f.read(10))
f.close()
