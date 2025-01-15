while True:
    input_s=input("What is your sentence? tape stop to exit the program ")
    if input_s=="stop":
        break
    input_search=input("what string you seach : ")
    print(input_search in input_s)
    
      


#--------------------------------------------
input_string = "Python is awesome"

print(input_string[0:3])
print(input_string[4:10])

# if the beginning index is left out, it defaults to 0
print(input_string[:3])

# if the end index is left out, it defaults to the length of the string
print(input_string[4:])
ex="My String My String"
ex2=ex[1:6]
print(ex2)

input_string = input("Please type in a string: ")
print("The tenth character: " + input_string[5])

mot="salam"
print(mot[-2])
input_string = input("Please type in a string: ")
index = 0
while index < len(input_string):
   print(input_string[index])
   index += 1


begin ="peaky"
end="Blinders"
word=begin+end
print(word)
print(word*3)
#Write a Python program that draw triangle in stars
n=10
row="*"
while n>0:
    print (" " * n + row)
    row+="**"
    n-=1
 
#len fonction:
word2="Elon musk And Sam Altman" #number of characters(meme les espaces)  
print (len(word2))
#calcule city citizens

nbrcity=int(input("how many city you will input : "))
while nbrcity<=0:
    nbrcity=int(input("how many city you will input : "))
    
#initialiser tableau
cities=[]   
count=0
while count< nbrcity:
    cityname=input("entrer le nom de la cite : ")   
    population = len(cityname) * 1000000
    cities.append((cityname,population))
    count+=1
#trier la liste une fonction sort()  pour trier les tableau  
cities.sort(key=lambda x: x[1], reverse=True)
print("Populations des villes (triées de la plus grande à la plus petite) :")
for city, population in cities:
        print(f"{city}: {population} citoyens")
#----------------------------------------------------------------
#string index:
ex="Hayat guendoul"  
print(ex[1])  
    
     
    



  
    

