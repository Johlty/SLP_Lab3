from colorama import Fore

def choose_color():
    colors = {
        "red": Fore.RED,
        "green": Fore.GREEN,
        "blue": Fore.BLUE,
        "yellow": Fore.YELLOW,
        "grey": Fore.LIGHTBLACK_EX,
        "white": Fore.WHITE,
    }
    print("Доступні кольори: red, green, blue, yellow, grey, white")
    while True:
        color_choice = input("Виберіть колір: ").lower()
        if color_choice in colors:
            return colors[color_choice]
        print("Невірний вибір кольору. Спробуйте ще раз.")
