def format_name(f_name, l_name):
    """
    Input: First Name and Last Name to format and return a title case version to yourself.
    """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("AnGEla", "YU"))
