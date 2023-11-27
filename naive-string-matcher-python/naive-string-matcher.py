print('\nNaive String Matcher by Raphael Light')

find_string = 'eye'
search_string = 'eceyeye'

valid_shift = 0
max_shift = len(search_string)-len(find_string)

for start in range(0, max_shift+1):
    end = start + len(find_string)
    if find_string == search_string[start:end]:
        valid_shift += 1

print(valid_shift)