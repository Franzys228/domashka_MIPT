with open('input.txt', 'r') as f:
    text = f.read()
count = 0
for char in text:
    if char in '.!?':
        count += 1
print(count)
