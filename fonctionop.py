def outer():
     x = "Hello"
     def inner():
        print(x) # Accessing enclosing scope
     inner()    
outer()       





def myfunction():
    print("Hello the fuction of Hayat")
myfunction()    
def hello(target):
    print("hello",target)
hello("hayat")
hello("Guendoul")
def sum(x,y):
    return x+y
print(sum(1,5))

counter = 0
def increment():
    global counter  # Declare as global
    counter=counter+1
    
increment()
print(counter) 





    