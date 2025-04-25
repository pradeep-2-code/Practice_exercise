def process_names(name_list):
    capitalized_names = [name.capitalize() for name in name_list]

    sorted_names = sorted(capitalized_names)

    result = ", ".join(sorted_names)

    return result
