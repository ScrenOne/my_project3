def capitalize_first_letters(input_string):
    """
    Capitalizes the first letter of each word in the input string.

    Args:
        input_string (str): The string to be processed.

    Returns:
        str: The input string with the first letter of each word capitalized.
    """
    return ' '.join(word.capitalize() for word in input_string.split())

