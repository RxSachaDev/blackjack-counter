import flet as ft
from view.blackjack_table_view import blackjack_table_view
from view.control_bar import control_bar

def main_window(page: ft.Page):
    page.title = "Blacjack Counter"
    page.window_width = 2000
    page.window_height = 1400
    page.add(
        ft.ShaderMask(
            content=ft.Text(
                "Blackjack Counter",
                size=36,
                weight=ft.FontWeight.BOLD,
            ),
            shader=ft.LinearGradient(
                begin=ft.alignment.center_left,
                end=ft.alignment.center_right,
                colors=[
                    "#FACC15",
                    "#FDE047",
                    "#EAB308",
                ],
            ),
            blend_mode=ft.BlendMode.SRC_IN,
        )
    )
    page.add(blackjack_table_view())
    page.add(control_bar())
    return main_window