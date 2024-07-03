import flet 
from flet import *

def main(page:Page):
    page.window_width = 300
    page.padding = 0
    page.spacing = 0
    Bar = Container(
        border_radius=border_radius.vertical(
            bottom=30
        ),
        shadow=BoxShadow(
            spread_radius=1,
            blur_radius=10,
            color="#fc4795",
        ),
        gradient = LinearGradient(
            begin=alignment.top_left,
            end=alignment.bottom_right,
            colors=["pink","white"]
        ),
        width = page.window_width,
        height = 150,
        padding = 10,
        content=Column(
            [
                Row(
                    [
                        IconButton(icon="menu",icon_size=25,icon_color="white"),
                        Text("Flet app",size=25,color="white",weight="bold"),
                        Row(
                            [
                                IconButton(icon="notifications",icon_size=25,icon_color="white"),
                                IconButton(icon="search",icon_size=25,icon_color="white"),


                            ],
                            alignment="spaceBetween",
                        )
                    ]
                )
            ]
        )
    )

    page.overlay.append(Bar)
    page.add(
        Column(
            [
                Container(
                    margin=margin.only(
                        top = page.window_height/2,
                    ),
                    alignment=alignment.center,
                    content=Column(
                        [
                            Text("Sample",size=30)
                        ]
                    )
                )
            ]
        )
    )
    page.update()
app(target=main)