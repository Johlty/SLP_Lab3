from input_handler import get_user_input, choose_font, choose_color
from art_generator import generate_ascii_art
from file_handler import save_to_file
from colorama import init

init(autoreset=True)  # Initialize Colorama

def format_output(ascii_art, color):
    print(color + ascii_art)

def main():
    while True:
        text = get_user_input()
        font = choose_font()
        color = choose_color()
        ascii_art = generate_ascii_art(text, font)
        format_output(ascii_art, color)

        if input("Бажаєте зберегти у файл? (y/n): ").lower() == 'y':
            save_to_file(ascii_art)

        restart_choice = input("Бажаєте перезапустити програму? (y/n): ").lower()
        if restart_choice != 'y':
            print("Дякую за використання програми!")
            break

if __name__ == "__main__":
    main()
