mot = input("type a word : ")
i = 0
j = len(mot) - 1  

while i <= j:  
    if mot[i] == mot[j]:
        i += 1
        j -= 1
    else:
        print(" pas un palindrome")
        break
else:  
    print(" un palindrome")
  
        
