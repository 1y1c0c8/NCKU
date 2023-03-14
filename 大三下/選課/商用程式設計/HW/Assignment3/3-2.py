print("~~~~~~~~~~~~~~~~~~~~~\n"+
      "This is Assignment3-2\n"+
      "~~~~~~~~~~~~~~~~~~~~~")

giveItATry = True
while(giveItATry):
    date = input("Please enter your birthday (mm/dd):")
    data = date.split('/')
    print("Your birth month is " + data[0] + " and the date is " + data[1])

    choice = input("Try again?(y/n)")
    choice = choice.lower()
    giveItATry = True if choice == "y" else False
print("##############\nclosing...\n##############")



