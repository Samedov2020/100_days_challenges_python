programming_dictionary={"name":"Famil","surname":"Samadov","age":23,"country":"Azerbaijan","target":"Get a Job in Dell,Intel,IBM or Microsoft"}
print(programming_dictionary["country"])

#Adding new item to the dictioany
programming_dictionary["name"]="Ramil"
print(programming_dictionary)

#Create an empty dictioany
empty_dictioanary={}

#Wipe an existing dictioany
programming_dictionary={}

#Edit an item in dictioany
programming_dictionary["target"]="You get an Job in Intel"
print(programming_dictionary)

#Loop through a dictioany
for thing in programming_dictionary:
    print(thing)