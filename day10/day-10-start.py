def format_name(f_name, l_name):
    '''
    Change the string with the first letter in captal and the rest in lower case
    '''
    formated_f_name = f_name.title() 
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

format_name ("CHRISTIAN", "MAGALHAES")