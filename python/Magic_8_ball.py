import random 
valor=random.randint(1,9)
pregunta=input("Ask a question: ")

if valor == 1:
    print("Magic 8 Ball: Yes - definitely.")
elif valor==2:
    print("Magic 8 Ball: It is decidedly so.")
elif valor==3:
    print("Magic 8 Ball: Without a doubt.")
elif valor==4:
    print("Magic 8 Ball: Reply hazy, try again.")
elif valor==5:
    print("Magic 8 Ball: Ask again later.")
elif valor==6:
    print("Magic 8 Ball: Better not tell you now.")
elif valor==7:
    print("Magic 8 Ball: My sources say no.")
elif valor==8:
    print("Magic 8 Ball: Outlook not so good.")
elif valor==9:
    print("Magic 8 Ball: Very doubtful.")