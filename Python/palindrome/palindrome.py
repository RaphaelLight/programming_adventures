print('\nPalindrome by Raphael Light')

while True:
    string = input("\nEnter a palindrome (type 'quit' to end the program): ")
    if string.lower() == 'quit':
        break

    string_list = string.split()
    formatted_string = " ".join(string_list)

    while True:
        if string.__contains__(' '):
            string = string.replace(' ', '')
        else:
            break

    reversed_string = "".join(reversed(string))

    if string.lower() == reversed_string.lower():
        print(f'\n{formatted_string.capitalize()} is a palindrome!')
    else:
        print(f'\n{formatted_string.capitalize()} is not a palindrome.')




