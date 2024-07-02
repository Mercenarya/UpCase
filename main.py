import flet as ft
from flet import View
import sqlite3
import datetime
import os

#Database Connection


db = sqlite3.connect('upcase.db',check_same_thread=False)
cursor = db.cursor()

#Test connection
try:
    if sqlite3.Connection:
        print("Connected")
    else:
        print("Not connected yet")
except sqlite3.Error as error:
    print(error)





def main(page: ft.Page):
    #--------------- BUILD DATABASE ------------------------- 
    def Display_Profile(e):
        Display_DB_Query = '''
            SELECT name,profession,company,status,birth
            FROM Profile
            WHERE id = 1
        '''
        try:
            cursor.execute(Display_DB_Query)
            print("all record Release")
            for obj in cursor.fetchall():
                Name = obj[0]
                Profession = obj[1]
                Company = obj[2]
                Status = obj[3]
                # Birthday = datetime.datetime.strptime(str(obj[4]), '%d-%m-%Y')
                # formatted = Birthday.strftime('%d-%m-%Y')
            NameDisplay.value = str(Name)
            professionDisplay.value = str(Profession)
            companyDisplay.value = str(Company)
            statusDisplay.value = str(Status)
            # birthDisplay.value = formatted
            db.commit()
        except sqlite3.Error as error:
            print(error)
        page.update()


    def Update_Profile(e):
        Display_Profile(e)      
        Update_DB_query = f'''
            UPDATE Profile 
            SET id = 1, name = '{Nameinput.value}', profession = '{Professioninput.value}',
            company = '{Companyinput.value}', status = '{Statusinput.value}', birth = {Birthday_select_text.value}
        '''
        Insert_DB_query = f'''
            INSERT INTO Profile (id,name,profession,company,status,birth)
            VALUES (?, ?, ?, ?, ?, ?)
        '''
        ID = 1
        Query_tube = (ID,str(Nameinput.value),str(Professioninput.value),
                      str(Companyinput.value),str(Statusinput.value),Birthday_select_text.value)
        try:
            cursor.execute(Update_DB_query)
            print("Command in process")
            Display_Profile(e)
            db.commit()
        except sqlite3.Error as error:
            print(error)
        
        page.update()



    
    #--------------- BUILD FUNCTION ------------------------- 
    #Birthday Selection
 
    def Birthday_selection(e):
        Birthday_select_text.value = f'{e.control.value.strftime('%d-%m-%Y')}'
        page.update()

    #Set up Date picker Variable    
    DatePickUp = ft.DatePicker(
        
        first_date=datetime.datetime(1950,1,1),
        last_date=datetime.datetime.now(),
        on_change=Birthday_selection,
        
    )

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
    Profession = ft.Icon(ft.icons.LOCAL_ATTRACTION_SHARP)
    company = ft.Icon(ft.icons.HOME)
    status = ft.Icon(ft.icons.VISIBILITY_OUTLINED)
    birth = ft.Icon(ft.icons.CALENDAR_TODAY)
    SaveProfile = ft.ElevatedButton("Save",color="white",bgcolor=ft.colors.PINK_200,on_click=Update_Profile)
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
    TimeSelectionButton = ft.IconButton(
        ft.icons.CALENDAR_MONTH,icon_color="white",
        on_click= lambda _: DatePickUp.pick_date()
    ) 
    Time_selection_layout = ft.Container(
        TimeSelectionButton,
        width=50,
        height=54,
        bgcolor="grey",
        margin=ft.margin.only(right=-10)
    )



    Birthday_select_text = ft.TextField(
        hint_text="0/0/0", hint_style=ft.TextStyle(color="grey"),
        width=200,height=55,color="grey",bgcolor=ft.colors.GREY_200,border_color=ft.colors.GREY_200
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
                                        ft.Row(
                                            [
                                                Time_selection_layout,
                                                Birthday_select_text
                                            ]
                                        )
                                        
                                        
                                    ],
                                    
                                )
                            ],
                            
                        ),
                        
                    ],
                    height=200,
                    scroll=ft.ScrollMode.ALWAYS
                ),
                SaveProfile
            ],
            
        ),
        height=300,
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
    
    

    page.overlay.append(DatePickUp)
    
    def route_change(e):
        page.views.clear
        page.views.append(
            View(
                "/Profile",
                [
                    ft.Row(
                        controls=[
                            Profile,
                            EditProfile
                        ]
                    ),
                    ActionEvent
                ],
                Display_Profile(e),
                bgcolor=ft.colors.PINK_100
            )
        )
        page.update()
    def view_pop(View):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.bgcolor = ft.colors.PINK_100
    page.update()

if __name__ == "__main__":
    ft.app(target=main,assets_dir='assets')