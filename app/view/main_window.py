import flet as ft
from view.blackjack_table_view import blackjack_table_view

def main_window(page: ft.Page):
    page.title = "Blacjack Counter"
    page.window_width = 1000
    page.window_height = 700
    page.add(blackjack_table_view())
    return main_window