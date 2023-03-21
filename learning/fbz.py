for num in range(1,100):
    if (num % 3) and (num % 5): print('fizzbuzz')
    elif (num % 3) and not (num % 5): print('fizz')
    elif (num % 5) and not (num % 3):print('buzz')
    else: print(num)
