# Functions with outputs

def format_name(f_name, l_name):
    name = "{f_name} {l_name}".format(f_name = f_name, l_name = l_name)

    return name.title()

print(format_name("john", "doE"))