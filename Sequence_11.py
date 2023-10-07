def capitalize_lines(input_lines):
    capitalized_lines = '\n'.join(line.strip().upper() for line in input_lines)
    return capitalized_lines
input_lines = []

print("Enter lines (type 'end' on a new line to stop input):")
while True:
    line = input()
    if line.lower() == 'end':
        break
    input_lines.append(line)
capitalized_lines = capitalize_lines(input_lines)
print("Output:")
print(capitalized_lines)
