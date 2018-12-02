from collections import Counter

# --- Part One ---

# What is the checksum for your list of box IDs?

input = open('../inputs/02_box_ids.txt').read().splitlines()

two_count = 0
three_count = 0
found_two = False
found_three = False

for word in input:
    char_count = Counter(word)
    char_list = char_count.values()
    found_two = False
    found_three = False

    for x in char_list:
        if x == 2 and not found_two:
            two_count += 1
            found_two = True
        elif x == 3 and not found_three:
            three_count += 1
            found_three = True

print('two_count: ', two_count)
print('three_count: ', three_count)

checksum = two_count * three_count

print(two_count, ' x ', three_count, ' = ', checksum)
