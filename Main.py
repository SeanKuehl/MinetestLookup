textFile = open("database.txt", "r")
entries = textFile.readlines()

userInput = ""

while userInput != "DONE":

    userInput = input("Enter something to search the database for or enter 'DONE' to quit: ")

    if userInput == "DONE":
        break

    for x in entries:
        if x.find(userInput) != -1:
            print(x)

textFile.close()