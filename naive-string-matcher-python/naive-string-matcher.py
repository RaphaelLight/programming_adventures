print('\nNaive String Matcher by Raphael Light')

while True:
    find_string = input('\nEnter the string to find: ')
    if find_string == '-999':
        break
    search_string = input('Enter the string to be searched: ')
    if search_string == '-999':
        break

    if len(find_string) >= len(search_string):
        print('\nFind string should be less than the search string.')
        continue

    valid_shift = 0
    max_shift = len(search_string)-len(find_string)

    for start in range(0, max_shift+1):
        end = start + len(find_string)
        if find_string == search_string[start:end]:
            valid_shift += 1

    print(f'\nThe number of {find_string} in {search_string} is {valid_shift}')