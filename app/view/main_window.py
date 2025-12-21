import flet as ft
from view.blackjack_table_view import blackjack_table_view
from view.control_bar import control_bar

def main_window() -> ft.Container:
    return ft.Container(
        width=2000,
        height=1400,
        content= ft.Row([
            ft.Column([
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
                ),
                blackjack_table_view(),
                control_bar(),
            ])
        ])
    )
