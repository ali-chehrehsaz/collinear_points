import colorama
from functools import wraps


def print_blue(text):
    print(f"{colorama.Fore.BLUE}{text}{colorama.Fore.RESET}")


def print_red(text):
    print(f"{colorama.Fore.RED}{text}{colorama.Fore.RESET}")


def print_yellow(text):
    print(f"{colorama.Fore.YELLOW}{text}{colorama.Fore.RESET}")


def print_green(text):
    print(f"{colorama.Fore.GREEN}{text}{colorama.Fore.RESET}")


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        output = func(*args, **kwargs)
        print_yellow(f'{func.__name__}({args}, {kwargs}) -> {output}')
        return output
    return wrapper
