import math
number=int(input("enter positive integer:"))
while number<=0:
    number = int(input("Enter a positive integer: "))
# Print the list of multiplication operations
i = 1
while i <= number:
    j = 1
    while j <= number:
        print(f"{i} x {j} = {i * j}")
        j += 1
    i += 1    
while True:
     number=int(input("please number  :"))
     if number ==-1:
         break
     while number>0:
         print(number)
         number-=1
    

sum=0
while True:
    number=int(input("please number ,-1 to exit :"))
    if number== -1:
        break
    if number>=100:
        continue
    sum+=number
print(f"sum is {sum}")    

number = int(input("Please type in a number: "))

while number != 10:
   print(number)
   number += 2

nb=int(input("entrer : "))
while nb<100 and nb%5 !=0:
    print(nb)
    nb +=3
print("Fin !!!!")    
while nb<10:
   print(nb)
   nb +=1
print("cest fini")   
   


while True:
    number = int(input("Enter a number: "))
    if number < 0:
        print("Invalid number")
    elif number > 0:
        sqrt_value = math.sqrt(number)
        print(f"The square root of {number} is: {sqrt_value:.2f}")  # Limit to 2 decimal places
    else:  # User entered 0
        break

print("End of procedure")   



while True:
    print("Hi")
    msg=input("should we contunue ? :")
    if msg=="No" :
        break
print("okay then")    
    



while True:
    number=int(input("input the numbre"))
    if number== -1:
        break
    print(number**2)
print("thank u bye")    