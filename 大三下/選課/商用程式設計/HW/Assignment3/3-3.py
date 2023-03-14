print("~~~~~~~~~~~~~~~~~~~~~\n"+
      "This is Assignment3-3\n"+
      "~~~~~~~~~~~~~~~~~~~~~")

giveItATry = True
while(giveItATry):
    id = input("Please enter your student id:")
    if(id[1] == "1"):
        print("grade 1")
    elif(id[1] == "0"):
        print("grade 2")
    elif(id[1] == "9"):
        print("grade 3")
    elif(id[1] == "8"):
        print("grade 4")
    
    choice = input("Try again?(y/n)")
    choice = choice.lower()
    giveItATry = True if choice == "y" else False
print("##############\nclosing...\n##############")