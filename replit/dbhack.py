InfoDb = []

InfoDb.append({
    "CountryName": "United States",
    "President": "Joe Biden",
    "Politicians":["Richard Burr", "Pat Toomey", "Rob Portman", "Richard Shelby", "Roy Blunt"]
})

InfoDb.append({
    "CountryName": "Mexico",
    "President": "Andrés Manuel López Obrador",
    "Politicians":["Venustiano Carranza", "Adolfo de la Huerta", "Álvaro Obregón", "Plutarco Elías Calles", "Emilio Portes Gil"]
})

InfoDb.append({
    "CountryName": "Portugal",
    "President": "Marcelo Rebelo de Sousa",
    "Politicians":["António Almeida Henriques", "António Alves Martins", "David José Alves", "Vítor Alves", "Albino Aroso"]
})

InfoDb.append({
    "CountryName": "Germany",
    "President": "Frank-Walter Steinmeier",
    "Politicians":["Otto von Bismarck", "Karl Dönitz", "Henry Alfred Kissinger", "Heinrich Luitpold Himmler", "Friedrich Wilhelm Viktor Albert"]
})
def print_data(n):
    print("CountryName", InfoDb[n]["CountryName"], "\nPresident", InfoDb[n]["President"])  # using comma puts space between values
    print("\t", "Politicians: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Politicians"]))  # join allows printing a string list with separator
    print()

# for loop iterates on length of InfoDb
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)


# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return


# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return


def driver():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion


