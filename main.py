
def calculate_resistance(resistances: list[int], parallel: bool):
    total_r = 0

    for r in resistances:
        if parallel:
            total_r += 1/r
        else:
            total_r += r

    return parallel and 1/total_r or total_r

def r_inputs():
    input_r = input("Input resistance: ")

    try:
        input_r = int(input_r)
    except ValueError:
        return
    
    return input_r

def new_resistance(parallel: bool):
    resistances = []

    while True:
        input_r = r_inputs()

        if input_r == None:
            break

        resistances.append(input_r)

    total_resistance = calculate_resistance(resistances, parallel)
    print(total_resistance)

def selections():
    selection = input("1: Resistance, 2: Current, 3: Voltage... Selection: ")

    if selection == "1":
        selection = input("1: Parallel, 2: Series... Selection: ")

        if selection == "1":
            new_resistance(True)
        else:
            new_resistance(False)
    elif selection == "2":
        return
    elif selection == "3":
        return

while True:
    selections()