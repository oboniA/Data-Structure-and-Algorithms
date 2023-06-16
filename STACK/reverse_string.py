"""
stack_template file is imported here
"""

import stack_template

string = ".tneduts a ma I dna rewonA inobO si eman yM"
rev_string = ""
s = stack_template.Stack()  # imported file activated

# append characters of string in stack
for char in range(len(string)):
    s.push(string[char])

# when stack has content
while not s.is_empty():
    # popped item added to the last state of reversed string
    rev_string += s.pop()

print(rev_string)
