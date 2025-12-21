import flet as ft

def card_dealer_widget() -> ft.Container:
    return ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.CLICK,
        content=ft.Container(
            width=64,
            height=96,
            border_radius=ft.border_radius.all(8),
            border=ft.border.all(2, "#4B5563"),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=["#374151", "#1F2937"],
            ),
            alignment=ft.alignment.center,
            content=ft.Image(
                src="assets/add_card.png",
                width=24,
                height=24,
                fit=ft.ImageFit.CONTAIN,
            )
        )
    )