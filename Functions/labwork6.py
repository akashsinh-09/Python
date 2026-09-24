def sum_product(*args):
    total = 0
    product = 1

    for num in args:
        total += num
        product *= num

    return total, product


s, p = sum_product(11, 12, 13, 14)

print("Sum:", s)
print("Product:", p)