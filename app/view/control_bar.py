import flet as ft

def control_bar() -> ft.Container:
    return ft.Container(
        width=984,
        height=70,
        content= ft.Column([
            ft.Row([
                ft.GestureDetector(
                    mouse_cursor=ft.MouseCursor.CLICK,
                    content=ft.Container(
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.center_left,
                            end=ft.alignment.center_right,
                            colors=["#CA8A04", "#EAB308"],
                        ),
                        border_radius=ft.border_radius.all(12),
                        padding=ft.padding.only(left=24, right=24, top=12, bottom=12),
                        content= ft.Row([
                            ft.Image(
                                src="assets/refresh.png",
                                width=16,
                                height=16,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            ft.Text("Réinitialiser", color="#111827", size=16, weight=ft.FontWeight.W_600)
                        ])
                    )
                ),
                ft.GestureDetector(
                    mouse_cursor=ft.MouseCursor.CLICK,
                    content=ft.Container(
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.center_left,
                            end=ft.alignment.center_right,
                            colors=["#16A34A", "#22C55E"],
                        ),
                        border_radius=ft.border_radius.all(12),
                        padding=ft.padding.only(left=24, right=24, top=12, bottom=12),
                        content= ft.Row([
                            ft.Image(
                                src="assets/photo.png",
                                width=16,
                                height=16,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            ft.Text("Détecter", color="#FFFFFF", size=16, weight=ft.FontWeight.W_600)
                        ])
                    )
                ),
                ft.GestureDetector(
                    mouse_cursor=ft.MouseCursor.CLICK,
                    content=ft.Container(
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.center_left,
                            end=ft.alignment.center_right,
                            colors=["#2563EB", "#3B82F6"],
                        ),
                        border_radius=ft.border_radius.all(12),
                        padding=ft.padding.only(left=24, right=24, top=12, bottom=12),
                        content= ft.Row([
                            ft.Image(
                                src="assets/mouse.png",
                                width=16,
                                height=16,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            ft.Text("Manuel", color="#FFFFFF", size=16, weight=ft.FontWeight.W_600)
                        ])
                    )
                ),
                ft.GestureDetector(
                    mouse_cursor=ft.MouseCursor.CLICK,
                    content=ft.Container(
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.center_left,
                            end=ft.alignment.center_right,
                            colors=["#374151", "#4B5563"],
                        ),
                        border_radius=ft.border_radius.all(12),
                        padding=ft.padding.only(left=24, right=24, top=12, bottom=12),
                        content= ft.Row([
                            ft.Image(
                                src="assets/settings.png",
                                width=16,
                                height=16,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            ft.Text("Paramètres", color="#FFFFFF", size=16, weight=ft.FontWeight.W_600)
                        ])
                    )
                )
            ], alignment=ft.MainAxisAlignment.CENTER)
        ], alignment=ft.MainAxisAlignment.CENTER)
    )