let1=input("input letter:")
let2=input("input letter:")
let3=input("input letter:")
letter=[let1,let2,let3]
letter.sort()
print(letter[1])

year=int(input("year :"))
if (year%4==0 and year%100 !=0) or year%400==0:
    print("this is a leap year.")
else:
    print("this year is a normal year")    


numb=int(input("enter number:"))
if numb%5==0 and numb%3==0:   
    print("fizzbuzz") 
elif numb%5==0:
    print("Buzz")
elif numb%3==0:
    print("Fizz")
