Gryffindor=0
Ravenclaw=0
Hufflepuff=0
Slytherin=0

print('===============')
print('The Sorting Hat')
print('===============')

# ~~~~~~~~~~~~~~~ Question 1 ~~~~~~~~~~~~~~~

q1=int(input("Q1) Do you like Dawn or Dusk?\n1)Dawn\n2)Dusk\n"))
if q1==1:
    Gryffindor+=1
    Ravenclaw+=1
elif q1==2:
    Hufflepuff+=1
    Slytherin+=1
else:
    print("Wrong input")

# ~~~~~~~~~~~~~~~ Question 2 ~~~~~~~~~~~~~~~

q2=int(input("Q2) When I'm dead,I want people to remember me as: \n1)The Good\n2)The Great\n3)The Wise\n4)The Bold\n"))
if q2==1:
    Hufflepuff+=2
elif q2==2:
    Slytherin+=2
elif q2==3:
    Ravenclaw+=2
elif q2==4:
    Gryffindor+=2
else:
    print("Wrong input")

# ~~~~~~~~~~~~~~~ Question 3 ~~~~~~~~~~~~~~~

q3=int(input("Q3) Which kind of instrument most pleases your ear? \n1)The violin\n2)The trumpet\n3)The piano\n4)The drum\n"))
if q3==1:
    Slytherin+=4
elif q3==2:
    Hufflepuff+=4
elif q3==3:
    Ravenclaw+=4
elif q3==4:
    Gryffindor+=4
else:
    print("Wrong input")

print("Gryffindor: ", Gryffindor)
print("Ravenclaw: ", Ravenclaw)
print("Hufflepuff: ", Hufflepuff)
print("Slytherin: ", Slytherin)

most_points = max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin)
print("================================================================")
print("YOU ARE PART OF!!!!!!!!!!!!")
if Gryffindor==most_points:
    print("Gryffindor!")
elif Ravenclaw==most_points:
    print("Ravenclaw!")
elif Hufflepuff==most_points:
    print("Hufflepuff!")
else:
    print("Slytherin!")
print("================================================================")
