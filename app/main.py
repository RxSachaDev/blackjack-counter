from view.main_window import main_window
import flet as ft

def main(page: ft.Page):
    page.title = "Blacjack Counter"
    page.add(main_window())

if __name__ == "__main__":
    ft.app(target=main)