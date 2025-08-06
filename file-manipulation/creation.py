import os

file1 = 'test_file1.txt'
with open(file1, 'w') as f:
    pass

file2 = open("test_file2.txt",'w')

file3 = "test_file3.txt"
with open(file3,'a') as f:
    f.write("This is a new line.\n")

file4 = open("test_file4.txt","w") #if it exists error

file5 = open("test_file5.txt","w") # goto line 11

# os.remove("test_file5.txt")

if os.path.exists("test_file5.txt"):
    print("found")
else:
    print("not found")

f = open("test_file3.txt")
print(f.read())