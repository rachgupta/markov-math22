from sys import argv

# Initialize an dictionary for arg inputs
texts = {}

# Populates the letters
for i in range(len(argv) - 1):
    text = open(argv[i + 1])
    texts[argv[i + 1]] = text.read()
    text.close()