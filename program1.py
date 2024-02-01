def return_divisible_num(num):
    """
    python code to test if number is divisible bt 5 and 7
    """
    for i in range(1,num):
        if i % 5 == 0 and i % 7 == 0:
            yield i 


