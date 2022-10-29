# # var_name = value --> comments

# name = "Kumar"
# price = 10.2972
# classCount = 7
# is_student = True

# print(name , type(name))

# print(price, type(price))

# print(classCount , type(classCount))

# print(is_student , type(is_student))


names = ["apple","mango","orange","apple","Python","Java","Python"]

#find the dup element. and also print the index.

for i in range(len(names)):
    for j in range(i+1,len(names)):
        if(names[i]==names[j]):
            print(j, names[j])
            break

names.sort()
print(names)