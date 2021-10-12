# Q. Write a program to print the following star pattern:
#       *
#      * *
#     * * *   for n = 3

def pattern(n):
    k = n - 1
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
 
n = 3
pattern(n)

# Output :      *   
#              * *  
#             * * *