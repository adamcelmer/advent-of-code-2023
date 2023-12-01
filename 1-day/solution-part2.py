#!python

nums = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
sum=0


def get_first_number(line: str):
    tmp = ""
    for char in line:
        if char.isdigit():
            return str(char)
        else:
            tmp += char
        for key, value in nums.items():
            if key in tmp:
                return str(nums[key])


def get_last_number(line: str):
    line_reversed = line[::-1]
    tmp = ""
    for char in line_reversed:
        if char.isdigit():
            return str(char)
        else:
            tmp = char + tmp
        for key, value in nums.items():
            if key in tmp:
                return str(value)


with open('input.txt') as file:
    while True:
        line = file.readline()
        if not line or line == "":
            break
        num1 = get_first_number(line)
        num2 = get_last_number(line)
        number = int(str(num1) + str(num2))
        sum += number

print(sum)
