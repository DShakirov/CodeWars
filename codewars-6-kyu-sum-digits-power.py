def compare_power_sum_of_digits_and_num(num):
    #ans = 0
    #for pow,val in enumerate(str(num)):
        #ans += int(val)**(int(pow)+1)
    return sum((int(val)**(int(pow)+1)) for pow,val in enumerate(str(num))) == num


def sum_dig_pow(a,b):
    return [i for i in range(a, b + 1) if compare_power_sum_of_digits_and_num(i)]

print(sum_dig_pow(1,100))