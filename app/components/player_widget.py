import flet as ft
from components.player_card_widget import player_card_widget    

def player_widget() -> ft.Container:
    return ft.Container(
        width=115,
        height=186,
        border_radius=ft.border_radius.all(12),
        border=ft.border.all(1, ft.Colors.with_opacity(0.3, "#EAB308")),
        bgcolor=ft.Colors.with_opacity(0.4, ft.Colors.BLACK),
        content= ft.Column([
            ft.Row([
                ft.Text("JOUEUR", color="#FACC15", size=12)
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([
                player_card_widget()
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([
                player_card_widget()
            ], alignment=ft.MainAxisAlignment.CENTER)
        ], alignment=ft.MainAxisAlignment.CENTER)
    )
    