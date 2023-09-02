# Functions with Outputs
def format_name(first_name, last_name):
    '''Takes first name and last name and return the title case version of the name'''
    full_name = first_name + " " + last_name
    return full_name.title()

f_name = input("Enter your Firstname: ")
l_name = input("Enter your Lastname: ")
format_name()