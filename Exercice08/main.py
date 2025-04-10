def log_decorator(func):
    def wrapper():
        print("Avant la fonction.")
        result = func()
        print("Après la fonction.")
        return result
    return wrapper

@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")

function_test()
