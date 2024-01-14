health=1
def increase():
    print(f"Standart health value {health}")
    return health+1
health=increase()
print(f"Increased health value {health}")