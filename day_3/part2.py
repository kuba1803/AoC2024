import re
sum = 0

def sumMul( text ):
    sum = 0
    listMul = re.findall(r'mul\(\d{1,3},\d{1,3}\)', text)
    for mul in listMul:
        num = re.findall(r'\d+', mul)
        sum += int(num[0]) * int(num[1])
    return sum


with open('input_file.txt') as f:
    content = f.read()
    list = re.split(r'don\'t\(\)', content);
    sum += sumMul(list[0])
    for i in range(1, len(list)):
        subList = re.split(r'do\(\)', list[i]);
        for j in range(1, len(subList)):
            sum += sumMul(subList[j])

print(sum)