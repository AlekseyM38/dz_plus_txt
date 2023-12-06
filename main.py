file_names = ['1.txt', '2.txt', '3.txt']

file_lines = {}

for file_name in file_names:
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file_lines[file_name] = len(lines)

sorted_files = sorted(file_lines.items(), key=lambda x: x[1])

with open('resume.txt', 'w', encoding='utf-8') as result_file:
    
    for file_info in sorted_files:
        file_name, lines_count = file_info
        result_file.write(f"{file_name}\n{lines_count}\n")
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                result_file.write(line)
        result_file.write('\n')