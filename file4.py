age=int(input("donne moi votre age :"))

if 5<=age<=18:
    print("you teenage or child")
elif age<5:
    print("you are too young")    
else:
    print("you are mature")  
word1=input("entrer premier mots :")
word2=input("entrer deuxieme mots :")
word3=input("entrer 3 mots :")
#first=min(word1,word2,word3)
if word1<word2 and word1<word3:
    first=word1
elif word2<word1 and word2<word3:
    fisrt=word2
else:
    first=word3       
print(first)
  

nb=int(input("donne moiun nombre :"))
if nb<0:
    print("number negative")
else:
    print("number positive ou nulle")    

if nb%2==0:
    print("nombre paire")    
else:
    print("nomre impaire")    