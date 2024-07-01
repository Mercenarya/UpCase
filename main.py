import flet as ft
import sqlite3


def main(page: ft.Page):

    #--------------- BUILD FUNCTION ------------------------- 
    #Offset animation
    def ActionNexttoEdit(e):
        Profile.offset = ft.transform.Offset(-2,0)
        EditProfile.offset = ft.transform.Offset(-1.03,0)
        NextAction.visible = False
        BackAction.visible = True
        ChangeSwitched.value = "Edit"
        animation_ref_1.width=60
        animation_ref_1.height=60
        animation_ref_1.animate_scale=ft.animation.Animation(duration=300,curve="bounceOut")
        animation_ref_1.scale = ft.transform.Scale(1)
        animation_ref_1.image_src="https://i.pinimg.com/originals/7e/83/13/7e831379147b6bcbdd05bc9dbb60352b.gif"
        Profile.update()
        EditProfile.update()
        page.update()

    def ActionBacktoProfile(e):
        

        Profile.offset = ft.transform.Offset(0,0)
        EditProfile.offset = ft.transform.Offset(2,0)
        NextAction.visible = True
        BackAction.visible = False
        ChangeSwitched.value = "Profile"
        animation_ref_1.width=50
        animation_ref_1.height=50
        animation_ref_1.animate_scale=ft.animation.Animation(duration=300,curve="bounceOut")
        animation_ref_1.scale = ft.transform.Scale(1)
        animation_ref_1.image_src="https://media2.giphy.com/avatars/tontonfriends/oR1fkkiDPgSG.gif"
        Profile.update()
        EditProfile.update()
        page.update()
    
   
    #--------------- CUSTOMIZE DESIGN VIEW -----------------
    #Text Actor 
    NameDisplay = ft.Text("Tran Hoang Minh",color="grey",weight="bold")
    professionDisplay = ft.Text("Mobile Developer",color="grey",weight="bold")
    companyDisplay = ft.Text("DVT Group",color="grey",weight="bold")
    statusDisplay = ft.Text("On work",color="grey",weight="bold")
    birthDisplay = ft.Text("11/10/1997",color="grey",weight="bold")
    
    ChangeSwitched = ft.Text("Profile",size=30,color="white")
    #Animation
    animation_ref_1 = ft.Container(
        image_src="https://media2.giphy.com/avatars/tontonfriends/oR1fkkiDPgSG.gif",
        width=50,
        height=50,
        
    )

    #Action button
    NextAction = ft.IconButton(
        ft.icons.NAVIGATE_NEXT,icon_color="white",
        icon_size=50,on_click=ActionNexttoEdit,visible=True
    )
    BackAction = ft.IconButton(
        ft.icons.NAVIGATE_BEFORE_SHARP,icon_color="white",
        icon_size=50,on_click=ActionBacktoProfile,visible=False
    )

    #Icon
    User = ft.Icon(ft.icons.ACCOUNT_BOX)
    Profession = ft.Icon(ft.icons.IMAGE_ASPECT_RATIO_OUTLINED)
    company = ft.Icon(ft.icons.HOME)
    status = ft.Icon(ft.icons.GIF_BOX)
    birth = ft.Icon(ft.icons.CALENDAR_TODAY)
    
    #TextField
    Nameinput = ft.TextField(width=250,height=50,color="grey",bgcolor=ft.colors.GREY_200,border_color=ft.colors.GREY_200)
    Professioninput = ft.TextField(width=250,height=50,color="grey",bgcolor=ft.colors.GREY_200,border_color=ft.colors.GREY_200)
    Companyinput = ft.TextField(width=250,height=50,color="grey",bgcolor=ft.colors.GREY_200,border_color=ft.colors.GREY_200)
    Statusinput = ft.Dropdown(
        width=250,
        height=60,
        hint_style=ft.TextStyle(color="grey"),
        hint_text="Choose",
        options=[
            ft.dropdown.Option("On work"),
            ft.dropdown.Option("Offline"),
            
        ],
        filled=True,
        border_color=ft.colors.GREY_200,
        color="grey",
        bgcolor=ft.colors.GREY_200
        
    )

    Birthday_select_text = ft.TextField(
        hint_text="0/0/0",
        hint_style=ft.TextStyle(color="grey"),
        prefix_icon=ft.IconButton(ft.icons.EDIT_CALENDAR_OUTLINED),
        width=250,height=50,color="grey",bgcolor=ft.colors.GREY_200,border_color=ft.colors.GREY_200
    )


    #Build Banner
    avt = ft.Container(
        image_src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRkPJ11D4Hn1el8cPpTbRkyBQB1FBIpPSyWEA&s",
        bgcolor="grey",
        border=ft.border.BorderSide(5,"black"),
        border_radius=100,
        height=150,
        width=150,

    )
    Editavt = ft.Container(
        image_src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRkPJ11D4Hn1el8cPpTbRkyBQB1FBIpPSyWEA&s",
        bgcolor="grey",
        border=ft.border.BorderSide(5,"black"),
        border_radius=100,
        height=150,
        width=150,

    )

    form = ft.Container(
        ft.Column(
            [
                
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Row(
                                    [
                                        User,
                                        NameDisplay
                                    ]
                                ),
                                ft.Row(
                                    [
                                        company,
                                        companyDisplay
                                    ]
                                ),
                                ft.Row(
                                    [
                                        status,
                                        statusDisplay
                                    ]
                                ),
                                ft.Row(
                                    [
                                        birth,
                                        birthDisplay
                                    ]
                                ),
                                ft.Row(
                                    [
                                        Profession,
                                        professionDisplay
                                    ]
                                ),
                                
                            ]
                        )
                    ],
                    
                )
            ]
        ),
        height=250,
        width=300,
        margin=ft.margin.only(left=20),
        padding=ft.padding.only(top=20,left=70),
       
        
    )
    Editform = ft.Container(
        ft.Column(
            [
                
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text("Name",color="grey",weight="bold"),
                                Nameinput,
                                ft.Text("Profession",color="grey",weight="bold"),
                                Professioninput,
                                ft.Text("Company",color="grey",weight="bold"),
                                Companyinput,
                                ft.Text("Status",color="grey",weight="bold"),
                                Statusinput,
                                ft.Text("Birthday",color="grey",weight="bold"),
                                Birthday_select_text
                                
                                
                            ],
                            
                        )
                    ],
                    
                )
            ],
            height=100,
            scroll=ft.ScrollMode.ALWAYS
        ),
        height=250,
        width=300,
        margin=ft.margin.only(left=20),
        padding=ft.padding.only(top=5,left=30),
        border_radius=20
        
    )
    Profile = ft.Container(
        ft.Column(
            [
                ft.Row(
                    [
                        avt
                    ],
                    alignment= ft.MainAxisAlignment.CENTER
                ),
                form
            ]
        ),
        width=340,
        height=500,
        bgcolor="white",
        border_radius=20,
        margin=ft.margin.only(top=30),
        padding=ft.padding.only(top=40),
        shadow= ft.BoxShadow(
            blur_radius=5,
            color="black",
            blur_style=ft.ShadowBlurStyle.OUTER
        ),
        offset=ft.transform.Offset(0,0),
        animate_offset=ft.animation.Animation(300)
    )

    

    
    EditProfile = ft.Container(
        ft.Column(
            [
                ft.Row(
                    [
                        Editavt
                    ],
                    alignment= ft.MainAxisAlignment.CENTER
                ),
                Editform
                
            ]
        ),
        width=340,
        height=500,
        bgcolor="white",
        border_radius=20,
        margin=ft.margin.only(top=30),
        padding=ft.padding.only(top=40),
        shadow= ft.BoxShadow(
            blur_radius=5,
            color="black",
            blur_style=ft.ShadowBlurStyle.OUTER
        ),
        offset=ft.transform.Offset(2,0),
        animate_offset=ft.animation.Animation(300)
    )
        
    
   
   
    
        
    
    
    ActionEvent = ft.Container(
        ft.Row(
            [
                animation_ref_1,
                ChangeSwitched,
                NextAction,
                BackAction
            ],
            alignment=ft.MainAxisAlignment.END
        )
    )
    
    

    
    page.add(
        ft.Row(
            controls=[
                Profile,
                EditProfile
            ]
        ),
        ActionEvent
    )

    page.bgcolor = ft.colors.PINK_100
    page.update()

if __name__ == "__main__":
    ft.app(target=main,assets_dir='assets')