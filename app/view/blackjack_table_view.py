import flet as ft
from components.card_widget import card_widget

def blackjack_table_view() -> ft.Container:
    table = ft.Container(
        width=984,
        height=632,
        bgcolor="#15803D",
        border_radius=ft.border_radius.all(16),
        padding=ft.padding.all(40),
        content=ft.Column([
            ft.Row([
                ft.Container(
                    width=186,
                    height=142,
                    bgcolor=ft.Colors.with_opacity(0.4, ft.Colors.BLACK),
                    border_radius=ft.border_radius.all(16),
                    border=ft.border.all(2, ft.Colors.with_opacity(0.3, "#EAB308")),
                    padding=ft.padding.all(3),
                    content=ft.Column([
                        ft.Row([
                            ft.Text("CROUPIER", color="#FACC15")
                        ], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([
                            card_widget(),
                            card_widget()
                        ], alignment=ft.MainAxisAlignment.CENTER)
                    ])
                )
            ], alignment=ft.MainAxisAlignment.CENTER),    
        ])
    )
    return table

