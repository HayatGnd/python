char=input("input String : ")
i=0
result=""
while i<len(char):
    result+=f" {char[i]}*"
    i+=1
print(result)    
    