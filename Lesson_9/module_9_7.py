def is_prime(func):
    def wrapper(*args):
        res_sum_three = func(*args)
        indicator = 0
        if res_sum_three >= 2:
            for i in range(2, res_sum_three):
                if res_sum_three % i == 0 and res_sum_three != 2:
                    indicator += 1
                    print('Cоставное')
                    break
            if res_sum_three == 2 or indicator == 0:
                print('Простое')
        else:
            print("Число не относится ни к простым, ни к составным")

        return res_sum_three

    return wrapper


@is_prime
def sum_three(*args):
    res = sum(args)
    return res


result = sum_three(2, 3, 6)
print(result)
