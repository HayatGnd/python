# Initialize an empty list
user_list = []

while True:
   
    user_input = input("Enter a number: ")
    
 
    if user_input.isdigit():
        number = int(user_input)
        
    
        if number == 0:
            break
        
      
        user_list.append(number)
        
       
        print(f"Current List: {user_list}")
        
        sorted_list = user_list[:]
        for i in range(1, len(sorted_list)):
            key = sorted_list[i]
            j = i - 1
            while j >= 0 and key < sorted_list[j]:
                sorted_list[j + 1] = sorted_list[j]
                j -= 1
            sorted_list[j + 1] = key
        print(f"Sorted List: {sorted_list}")
    else:
        print("Please enter a valid integer.")
        
print("Program terminated.")

   
    