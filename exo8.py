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