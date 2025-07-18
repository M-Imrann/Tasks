from functools import wraps


def repeat(n, print_result=True):
    '''
    repeat function for repeating the specific function for 'n' number of time.

    Args:
    n : N is for that how many times our function will repeat.

    Return: return the decorated function.
    '''
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for i in range(n):
                result = func(*args, **kwargs)
                results.append(result)
            return results

        return wrapper
    return decorator


@repeat(3, print_result=True)
def greeting(name):
    return f"Hey {name}"


print(greeting("Ali"))
