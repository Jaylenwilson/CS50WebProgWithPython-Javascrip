#  set - collection of unique values its is mutable
# Create an empty set
s = set()

# Add elements to set
# no element appears more than once in a set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(s)

# remove elements from set
s.remove(2)
print(s)

# len gives the length of a sequence
# How many elements are in the set
print(f"The set has {len(s)} elements.")
