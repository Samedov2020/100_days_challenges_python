def my_function():
    result=3*2
    return result
  
  #Functions with output  
def name_format(f_name,l_name):
    print(f_name.title())
    print(l_name.title())
name_format("RaMil","RAMIL")

def name_format(f_name,l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    print(f"{formated_f_name} {formated_l_name}")
name_format("RaMil","SAMADOV")