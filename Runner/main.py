import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Interface.input_handler import get_user_input
from Functions.art_generator import generate_ascii_art
from Interface.output_formatter import format_output
from FileHandler.file_handler import save_to_file
from Functions.font_selector import choose_font  
from Functions.color_selector import choose_color  
from colorama import init

init(autoreset=True)

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
