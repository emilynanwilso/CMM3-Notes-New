def calculate(func,lower_limit, upper_limit, interval_limit ):
    interval_size = (upper_limit - lower_limit) / interval_limit
    sum = func(lower_limit) + func(upper_limit);
    #Calculates value till integral limit
    for i in range(1, interval_limit ):
        if (i % 3 == 0):
            sum = sum + 2 * func(lower_limit + i * interval_size)
        else:
            sum = sum + 3 * func(lower_limit + i * interval_size)
    return ((float( 3 * interval_size) / 8 ) * sum )
    
def func(x):
    return x**2 + 4*x - 12

integral_res = calculate(func,-10, 10, 30)
print(integral_res)