from colorama import Fore
def get_user_input():
    return input("Введіть слово або фразу для ASCII-арту: ")

def choose_font():
    fonts = ['standard', 'slant', '3-d', '5lineoblique']
    print("Доступні шрифти:")
    for i, font in enumerate(fonts):
        print(f"{i + 1}. {font}")
    while True:
        try:
            choice = int(input("Виберіть номер шрифту: ")) - 1
            return fonts[choice]
        except (ValueError, IndexError):
            print("Невірний вибір. Спробуйте ще раз.")

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
