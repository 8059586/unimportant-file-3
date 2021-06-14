def countwords():
    name = input("Enter file name: ")
    number = 0
    file = open(name,"r")
    for i in file:
        words = i.split()
        number = number+len(words)
    print(number)

countwords()

# def - used to create functions 
# input - accepts the input value from the user
# open - is used to open the file. r indicates the file is in read format
# spilt - splits the line when there is a space
#len - counts the number of values in a list
