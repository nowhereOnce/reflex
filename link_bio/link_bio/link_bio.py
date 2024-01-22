import reflex as rx

class State(rx.State):
    pass



def index() -> rx.Component:
    return rx.hstack(
        rx.text(
            "NowhereOnce",
            ),
        position = "sticky",
        bg = "blue",
        z_index = "999",
        padding = "20px"
    )


app = rx.App()
app.add_page(index)