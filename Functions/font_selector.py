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
