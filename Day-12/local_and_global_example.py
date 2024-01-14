#Scope Global and Local 

#Global scopes are available both inside and outside the function.but Local scopes are available only inside the function
# Additionally it is not a good idea to call the local and global variables with same name 'enemies'

enemies="Zombie"

def local():
    enemies="Skeleton"
    print(f"Local Scope - Enemies inside the function : {enemies}")
    
local()

print(f"Global Scope - Enemies outside the function : {enemies}")