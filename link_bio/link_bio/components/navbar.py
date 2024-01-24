import reflex as rx


def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "NowhereOnce",
            ),
        position = "sticky", #para que mantenga su posicion
        bg = "blue", #color de fondo del he
        z_index = "999", #posicion de prioridad (layer)
        padding = "20px" #Espaciado hacia adentro
    )