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
                    content=ft.Column([
                        ft.Row([
                            ft.Text("CROUPIER", color="#FACC15", size=12)
                        ], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([
                            card_widget(),
                            card_widget()
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
            ], alignment=ft.MainAxisAlignment.CENTER)    
        ], spacing=40)
    )
    return table

