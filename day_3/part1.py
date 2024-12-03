import re
sum = 0

with open('input_file.txt') as f:
    for line in f:
        listMul = re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)
        for mul in listMul:
            num = re.findall(r'\d+', mul)
            sum += int(num[0]) * int(num[1])

print(sum)