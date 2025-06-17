def strict(func):
    def wrapper(*args,**kwargs):
        dict_of_args = func.__annotations__ # Это словарь, в котором ключи это названия аргументов, а значения это типы аргументов
        arr_of_args = [i for i in dict_of_args] # Это список ключей словаря. он нужен, чтобы можно было перебрать значения словаря

        for i in range(len(args)):
            if dict_of_args[arr_of_args[i]] != type(args[i]):
                raise TypeError(f'Аргумент "{arr_of_args[i]}" соответствует типу {type(args[i])}, а он должен соответствовать типу {dict_of_args[arr_of_args[i]]} , как показано в аннотациях')
        
        result = func(*args, **kwargs)
        return result
    return wrapper
        

# Можно раскомментировать функции снизу, чтобы проверить декоратор


# @strict
# def print_four_numbers(a: int, b: float, c: str, d: bool) -> str:
#     nums = f"{a}, {b}, {c}, {d}"
#     print(nums)
#     return nums

# @strict
# def wrong_print_four_numbers(a: int, b: float, c: str, d: bool) -> str:
#     nums = f"{a}, {b}, {c}, {d}"
#     print(nums)
#     return nums

    
# print_four_numbers(1, 43.42, 'hello', True)
# wrong_print_four_numbers('1', 43.42, 'hello', 1)