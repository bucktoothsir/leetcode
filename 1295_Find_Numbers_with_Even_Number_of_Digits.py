def get_digits(num):
    num_of_digits = 0
    while num:
        num_of_digits += 1
        num //= 10
    return num_of_digits

def findNumbers(nums):
    num_of_even_digits = 0
    for num in nums:
        if get_digits(num) % 2 == 0:
            num_of_even_digits += 1
    return num_of_even_digits

if __name__ == '__main__':
    nums = [12,345,2,6,7896]
    print(findNumbers(nums))