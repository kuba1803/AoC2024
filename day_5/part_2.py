import math

sum = 0
rules = []
pages = []


def valid_rules(page, rules, idx):
    for rule in rules:
        if (page[idx] == rule[0]):
            for revIdx in range(0, idx):
                if (page[revIdx] == rule[1]):
                    return False
    return True


def valid_page(page, rules):
    for idx in range(len(page)):
        if (not valid_rules(page, rules, idx)):
            return False
    return True


def sort(page, rules):
    isSorted = valid_page(page, rules)
    while (not isSorted):
        for idx in range(1, len(page)):
            if (not valid_rule(page, rules, idx)):
                page[idx], page[idx - 1] = page[idx - 1], page[idx]
        isSorted = valid_page(page, rules)


with open('input_file.txt') as f:
    for line in f:
        if line != "\n":
            if ("|" in line):
                rules.append(list(map(int, line.strip().split('|'))))
            else:
                pages.append(list(map(int, line.strip().split(','))))

    for page in pages:
        if (not valid_page(page, rules)):
            sort(page, rules)
            sum += page[math.floor(len(page) / 2)]

print(sum)
