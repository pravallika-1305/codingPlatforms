def is_palindrome(num):
    num = str(num)
    return num == num[::-1]

def palindrome_product():
    product = list(i * j for i in range(1000,100,-1) for j in range(1000,100,-1) if is_palindrome(i*j))
    return product

def largest_product():
    palindrome_list = palindrome_product()
    maximum_product =  max(palindrome_list)
    return maximum_product

print(largest_product())


