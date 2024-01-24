#vista que contiene de forma vertical los links
import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Twitch",  "https://twitch.tv/werehog89"),
        link_button("Instagram",  "https://www.instagram.com/n.ow.here?igsh=MXFjbmRzY2hvcnFpdQ=="),
        link_button("GitHub", "https://github.com/nowhereOnce")
    )