def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

def ispal(num):
    return str(num) == str(num)[::-1]