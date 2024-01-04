def format_name(f_name,l_name):
    if f_name=="" or l_name=="":
        return "You didn't provide valid input"
    format_f_name=f_name.title()
    format_l_name=l_name.title()
    return f"{format_l_name} {format_f_name}"
    print("This got printed")   #This will not print,because return says it is end of the function
print(format_name(input("What is your name? "),input("What is your surname? ")))