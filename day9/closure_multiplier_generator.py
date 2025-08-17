def multiplier_generator(base):
    if base == 0:
        def square(num):
            return num * num
        return square
    else:
        def multiplier(num):
            return base * num
        return multiplier


doubler = multiplier_generator(2)
tripler = multiplier_generator(3)
squarer = multiplier_generator(0)

print("[Closure] Doubler(5):", doubler(5))     
print("[Closure] Tripler(4):", tripler(4))    
print("[Closure] Squarer(6):", squarer(6))      