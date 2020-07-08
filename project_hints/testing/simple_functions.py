def function_1():
    return "Output for function 1."


def function_2():
    return "Correct output for function 2."


# def function_3(x):
    # return (f"x = {x}")

def function_3(name):
    if isinstance(name, int):
        # print('x is a int!')
        name = int(name)
    elif isinstance(name, float):
        # print('x is a float!')
        name = float(name)
        name = format(name, '.2f')
    elif isinstance(name, str):
        # print('x is a str!')
        name = str(name)
    
    output = f"x = {name}"
    return output

def function_4(x, y):
    x=float(x)
    y=float(y)
    return x + y

