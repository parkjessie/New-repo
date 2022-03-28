from replit import dbhack

main_menu = [
    ["matrix", "replit/matrix.py"],
    ["swap", "replit/swap.py"],
    ["Fibonacci Sequence", "replit/fibonacci.py"],
    ["Loop", "replit/dbhack.py"]
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
animationsub_menu = [
    ["Boat animation", "replit/boat.py"],
    ["Person animation", "replit/tree.py"]
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
    buildMenu(title, menu_list)


if __name__ == "__main__":
    menu()