with open('input.txt') as file:
    numbers_line = file.readline().strip()
    operation = file.readline().strip()
numbers = list(map(int, numbers_line.split()))
a, b = numbers[0], numbers[1]
if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
output_line = f"Result of {operation} operation with {a} and {b}:\n{result}"
with open('output.txt', 'w') as file:
    file.write(output_line)
