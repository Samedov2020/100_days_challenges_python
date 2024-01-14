#Modify the global variable inside the function
health=1

def increase():
    global health
    health+=1
    print(f"Health inside the function {health}")
increase()
print(f"Health outside the function {health}")