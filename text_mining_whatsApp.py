import re


file_path = '/content/input_file.txt'
with open(file_path, "r") as f:
    lines = f.readlines()
    
pattern = "Indian Central Laboratory Project Number [0-9X]{1,}"
match_list = []

for line in lines:
    matches = re.findall(pattern, line)
    for match in matches:
        match_list.append(match)
