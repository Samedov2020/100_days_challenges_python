#Scope Global and Local 

#Global scopes are available both inside and outside the function.but Local scopes are available only inside the function

player_health=10  #global scope

def drink_potion():
    lost_health=90
    print(lost_health) #local scope
    print(player_health)
drink_potion()