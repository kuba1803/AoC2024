import math

sum = 0
rules = []
pages = []


def valid_page(page, rules):
    for idx in range(len(page)):
        for rule in rules:
            if (page[idx] == rule[0]):
                for revIdx in range(0, idx):
                    if (page[revIdx] == rule[1]):
                        return False
    return True


with open('input_file.txt') as f:
    for line in f:
        if line != "\n":
            if ("|" in line):
                rules.append(list(map(int, line.strip().split('|'))))
            else:
                pages.append(list(map(int, line.strip().split(','))))

    for page in pages:
        if (valid_page(page, rules)):
            sum += page[math.floor(len(page) / 2)]

print(sum)
