import flet as ft
from components.dealer_card_widget import card_dealer_widget
from components.player_widget import player_widget

def blackjack_table_view() -> ft.Container:
    table = ft.Container(
        width=984,
        height=632,
        bgcolor="#15803D",
        border_radius=ft.border_radius.all(16),
        content=ft.Column([
            ft.Row([
                ft.Container(
                    width=186,
                    height=142,
                    bgcolor=ft.Colors.with_opacity(0.4, ft.Colors.BLACK),
                    border_radius=ft.border_radius.all(16),
                    border=ft.border.all(2, ft.Colors.with_opacity(0.3, "#EAB308")),
                    content=ft.Column([
                        ft.Row([
                            ft.Text("CROUPIER", color="#FACC15", size=12)
                        ], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([
                            card_dealer_widget(),
                            card_dealer_widget()
                        ], alignment=ft.MainAxisAlignment.CENTER)
                    ], alignment=ft.MainAxisAlignment.CENTER)
                )
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([
                ft.Container(
                    width=235,
                    height=96,
                    border_radius=ft.border_radius.all(16),
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.center_left,
                        end=ft.alignment.center_right,
                        colors=["#EAB308", "#FACC15", "#EAB308"],
                    ),
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=10,
                        color=ft.Colors.with_opacity(0.3, "#000000"),
                        offset=ft.Offset(4, 4),
                    ),
                    content= ft.Column([
                        ft.Row([
                            ft.Text("ACTION RECOMMANDÉE", color=ft.Colors.BLACK, size=12),
                        ], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([
                            ft.Text("STAND", color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD, size=36),
                        ], alignment=ft.MainAxisAlignment.CENTER)
                    ], alignment=ft.MainAxisAlignment.CENTER, spacing=0)
                )
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([
                player_widget(),
            ], alignment=ft.MainAxisAlignment.CENTER),    
        ], spacing=40, alignment=ft.MainAxisAlignment.CENTER)
    )
    return table

