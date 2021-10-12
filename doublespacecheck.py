# Q. Write a program to detect double spaces in a string

string = input("Enter String: ")
res = "  " in string
print("Does string contain spaces ? " + str(res))

# Output: Enter String: Gaurav Shardul                     //with 2 spaces
#         Does string contain spaces ? True  

#         Enter String: Gaurav Shardul                    //with 1 space
#         Does string contain spaces ? False 
