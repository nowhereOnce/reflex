import reflex as rx
from link_bio.components.navbar import navbar #importamos la navbar desde su directorio
from link_bio.views.header.header import header
from link_bio.views.header.links import links
from link_bio.components.footer import footer


class State(rx.State):
    pass



def index() -> rx.Component:
    #la funcion index tiene que devolver un componente de reflex
    #en este caso un contenedor general vstack(general)
    return rx.vstack(
        navbar(), #barra de navegacion superior
        header(),
        links(),
        footer()
        )


app = rx.App()
app.add_page(index)