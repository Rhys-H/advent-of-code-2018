import re
from collections import defaultdict

# --- Part One ---

# All claims have an ID and consist of a single rectangle with edges parallel to the edges of the
# fabric. The problem is that many of the claims overlap, causing two or more claims to cover part
# of the same areas.
# How many square inches of fabric are within two or more claims?

input = open('../inputs/03_fabric_claims.txt').read().splitlines()

claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), input)

point = defaultdict(list)
overlaps = {}

for (claim_number, start_x, start_y, width, height) in claims:
  overlaps[claim_number] = set()
  for x in range(start_x, start_x + width):
    for y in range(start_y, start_y + height):
      if point[(x, y)]:
        for number in point[(x, y)]:
          overlaps[number].add(claim_number)
          overlaps[claim_number].add(number)
      point[(x, y)].append(claim_number)

contested_count = len([k for k in point if len(point[k]) > 1])
unique_id = [k for k in overlaps if len(overlaps[k]) == 0][0]

print('----------------')
print('Part 1: ', contested_count)
print('----------------')


# --- Part Two ---

# What is the ID of the only claim that doesn't overlap?

print('----------------')
print('Part 2: ', unique_id)
print('----------------')
