import dbhack
from lcm import *

main_menu = [
    ["Loop", "dbhack.py"]
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
animationsub_menu = [
    ["Boat animation", "rep/week0/boat.py"],
    ["Person animation", "rep/week0/tree.py"],
    ["Pyramid animation", "rep/week0/pyramid.py"]
]

mathsub_menu = [
    ["Fibonacci", "rep/week1/fibonacci.py"],
    ["matrix", "rep/week0/matrix.py"],
    ["swap", "rep/week0/swap.py"],
    ["Least Common Multiple", "lcm.py"],
    ["Factorial", "rep/week2/factorial.py"],
    ["Palindrome", "palindrome.py"]
]

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"



def buildMenu(banner, options):
    print(banner)
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op
    for key, value in prompts.items():
        print(key, '->', value[0])
    choice = input("Type your choice> ")
    try:
        choice = int(choice)
        if choice == 0:
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid choice: {choice}")
    buildMenu(banner, options)

def animationsubmenu():
    title = "Function Submenu" + banner
    buildMenu(title, animationsub_menu)


def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Animations", animationsubmenu])
    menu_list.append(["Math", mathsubmenu])
    buildMenu(title, menu_list)

def mathsubmenu():
    title = "Function Submenu" + banner
    buildMenu(title, mathsub_menu)


if __name__ == "__main__":
    menu()