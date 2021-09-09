# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["1"],
        ["","1 = 1","La suma de la serie es: 1"],
        "TC1 - Debe salir: La suma de la serie es: 1"
    ),
    # Test case 2
    (
        ["2"],
        ["","1 = 1","1 + 2 = 3","La suma de la serie es: 4"],
        "TC2 - Debe salir: La suma de la serie es: 4"
    ),
    # Test case 3
    (
        ["-3"],
        ["","El número es inválido"],
        "TC3 - Debe salir: El número es inválido"
    ),
    # Test case 4
    (
        ["10"],
        ["","1 = 1","1 + 2 = 3","1 + 2 + 3 = 6","1 + 2 + 3 + 4 = 10","1 + 2 + 3 + 4 + 5 = 15","1 + 2 + 3 + 4 + 5 + 6 = 21","1 + 2 + 3 + 4 + 5 + 6 + 7 = 28","1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36","1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45","1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55","La suma de la serie es: 220"],
        "TC4 - Debe salir: La suma de la serie es: 220"
    ),
    # Test case 5
    (
        ["0"],
        ["","El número es inválido"],
        "TC5 - Debe salir: El número es inválido"
    )
    ]
