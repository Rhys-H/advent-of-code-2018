# --- Part One ---

# Starting with a frequency of zero, what is the resulting frequency after all
# of the changes in frequency have been applied?.

with open('../inputs/01_device_frequencies.txt') as file:
    input = [int(x) for x in file]

print('----------------')
print('Part 1: ', sum(input))
print('----------------')


# --- Part Two ---

# You notice that the device repeats the same frequency change list over and over. To calibrate the
# device, you need to find the first frequency it reaches twice.

current_frequency = 0
obtained_frequencies = [current_frequency]
found = False

while not found:
  for index, i in enumerate(input):
    current_frequency = current_frequency + i

    if current_frequency not in obtained_frequencies:
      obtained_frequencies.append(current_frequency)
    else:
      found = True
      break
  if found:
    break

print('----------------')
print('Part 2: ', current_frequency)
print('----------------')
