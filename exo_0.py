numpeo=int(input("How many people need a ride ? : "))
#il faut un nombre positive
while numpeo<=0:
    numpeo=int(input("How many people need a ride ? : "))
    
numpint=int(input("how many people in one taxi ? : "))
while numpint<=0:
    numpeo=int(input("how many people in one taxi ? : "))
if numpeo % numpint!=0:
    numtax=numpeo//numpint+1  #il faut la valeur entiere plus 1
else:
    numtax=numpeo/numpint
print(f"the numbre of taxi is : {numtax}")  
  
        
    
        

   
    