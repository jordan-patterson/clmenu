from clmenu import Menu

options=["option1","option2","option3","option4"]
instructions="This is a test"

filename="/home/jordan/Desktop/priority/frequently/logo.txt"

menu=Menu(options,instructions,filename)
temp=menu.prompt()
print("You selected "+options[temp])