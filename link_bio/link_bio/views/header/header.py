#Esta es una view que se compone de el avatar y el texto
#introductorio a la página con mi presentación
import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Alejandro Aguilar", size="xl"),
        rx.text("@nowhereOnce"),
        rx.text("Hola mi nombre es Alejandro Aguilar 👋"),
        rx.text("Soy un ingeniero de software que está aprendiendo a como hacer una página web con reflex")
    )