height=int(input("How tall are you? "))
credits=int(input("How many credits do yo have? "))

if credits > 10:
    if height >=120137:
        print("Enjoy the ride!")            
    else:
        with_taller_person=bool(input("Are you with a taller person?"))
        if height <=100 or with_taller_person==True:
            print("Enjoy the ride!")
        else:  
            print("You're not tall enough for this ride yet!")
else:           
    print("You don't have enough credits")