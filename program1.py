def return_divisible_num(num):
    for i in range(1,num):
        if i % 5 == 0 and i % 7 == 0:
            yield i 


