import flet
from flet import *
from functools import partial
import time




class ModernNavBar(UserControl):
    def __init__(self,func):
        self.func = func
        super().__init__()


    def HighLight(self,e):
        print("e = "+str(e.data))
        if e.data == "true":
            print("girdi")
            e.control.bgcolor = "white10"
            e.control.update()

            e.control.content.controls[0].icon_color = "white"
            e.control.content.controls[1].color = "white"
            e.control.content.update()
        else:

            e.control.bgcolor=None
            e.control.update()

            e.control.content.controls[0].icon_color = "white54"
            e.control.content.controls[1].color = "white54"
            e.control.content.update()

    def UserData(self,initialise:str,name:str,description:str):

        return Container(
            content=Row(
                controls=[
                    Container(
                        width=42,
                        height=42,
                        bgcolor="bluegrey900",
                        alignment=alignment.center,
                        border_radius=8,
                        content=Text(
                            color="white",
                            value=initialise,
                            size=20,
                            weight="bold",
                        ),
                    ),
                    Column(
                        alignment=MainAxisAlignment.CENTER,
                        spacing=1,
                        controls=[
                            Text(
                                color="white",
                                value=name,
                                size=11,
                                weight="bold",
                                opacity=1,
                                animate_opacity=200,

                            ),
                            Text(
                                color="white54",
                                value=description,
                                size=9,
                                weight="bold",
                                opacity=1,
                                animate_opacity=200,

                            ),
                        ]
                    )
                ]
            )
        )
    def ContainedIcon(self,icon_name:str,text:str):
        return Container(
            width=180,
            height=45,
            border_radius=10,
            on_hover=lambda e: self.HighLight(e),
            on_click=None,
            content=Row(
                controls=[
                    IconButton(
                        icon=icon_name,
                        icon_size=18,
                        icon_color="white54",
                        style=ButtonStyle(
                            shape={
                                "":RoundedRectangleBorder(radius=7)
                            },
                            overlay_color={"":"transparent"}

                        )
                    ),
                    Text(
                        color="white54",
                        value=text,
                        size=9,
                        weight="bold",
                        opacity=1,
                        animate_opacity=200,

                    ),
                ]
            )
        )

    def build(self):
        return Container(
            width=200,
            height=580,
            padding=padding.only(top=10),
            alignment=alignment.center,

            content=Column(
                alignment=MainAxisAlignment.START,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    self.UserData("LI","Line Indent","Software"),
                    Container(
                        width=24,
                        height=24,
                        bgcolor="bluegrey800",
                        border_radius=8,
                        on_click=self.func

                    ),
                    Divider(height=5,color="transparent"),
                    self.ContainedIcon(icons.DASHBOARD,"Dashboard"),
                    self.ContainedIcon(icons.ANALYTICS, "Analytics"),

                    Divider(height=50,color="white24"),
                    self.ContainedIcon(icons.SETTINGS, "Settings"),

                ]
            )
        )


def main(page: Page):
    page.title = "Flet Modern Sidebar"

    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    def AnimateSideBar(e):
        if page.controls[0].width != 62:
            for item in (
                    page.controls[0]
                            .content.controls[0]
                            .content.controls[0]
                            .content.controls[1]
                            .controls[:]
            ):
                item.opacity = 0
                item.update()

            for items in page.controls[0].content.controls[0].content.controls[3:]:
                if isinstance(items, Container):
                    items.content.controls[1].opacity = 0
                    items.content.update()
            time.sleep(0.2)

            page.controls[0].width = 62
            page.controls[0].update()
        else:

            page.controls[0].width = 200
            page.controls[0].update()

            time.sleep(0.2)

            for item in (
                    page.controls[0]
                            .content.controls[0]
                            .content.controls[0]
                            .content.controls[1]
                            .controls[:]
            ):
                item.opacity = 1
                item.update()

            for items in page.controls[0].content.controls[0].content.controls[3:]:
                if isinstance(items, Container):
                    items.content.controls[1].opacity = 1
                    items.content.update()


    page.add(Container(
        content=ModernNavBar(AnimateSideBar),
        padding=10,
        width=200,
        height=580,
        bgcolor="black",
        border_radius=20,
        alignment=alignment.center,
        animate = animation.Animation(500, "decelerate")

    ))

    page.update()
    print(str(page.controls[0]))


if __name__ == "__main__":
    flet.app(target=main)