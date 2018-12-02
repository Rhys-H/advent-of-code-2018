from collections import Counter
from difflib import SequenceMatcher

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

checksum = two_count * three_count

print('----------------')
print('Part 1: ', checksum)
print('----------------')


# --- Part Two ---

# The boxes will have IDs which differ by exactly one character at the same
# position in both strings.
# What letters are common between the two correct box IDs?

found_match = False

similarity_threshold = (len(input[0]) - 1) / len(input[0])

for word in input:
    for compare_word in input:
        similarity = SequenceMatcher(None, word, compare_word).ratio()
        if similarity == similarity_threshold:
            found_match = True
            break

    if found_match:
        break

box_id = [i for i, j in zip(word, compare_word) if i == j]

box_id = ''.join(box_id)

print('----------------')
print('Part 2: ', box_id)
print('----------------')
