import flet as ft
from flet import View
import sqlite3
import datetime
import time
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
                Birthday = obj[4]
                # Birthday = datetime.datetime.strptime(str(obj[4]), '%Y-%m-%d').strftime('%Y-%m-%d')
                NameDisplay.value = str(Name)
                professionDisplay.value = str(Profession)
                companyDisplay.value = str(Company)
                statusDisplay.value = str(Status)
                birthDisplay.value = f'{Birthday}'
            print(Birthday)
            db.commit()
        except sqlite3.Error as error:
            print(error)
        page.update()

    
    def Update_Profile(e):
        # Date_str = birthDisplay.value
        # Converted_date = datetime.datetime.strptime(Date_str, '%Y-%m-%d')
        # Release_date = Converted_date.strftime('%Y-%m-%d')
            
        Update_DB_query = f'''
            UPDATE Profile 
            SET  name = '{Nameinput.value}', profession = '{Professioninput.value}',
            company = '{Companyinput.value}', status = '{Statusinput.value}', birth = '{Birthday_select_text.value}'
            WHERE id = 1
        '''
        Insert_DB_query = f'''
            INSERT INTO Profile (id,name,profession,company,status,birth)
            VALUES (?, ?, ?, ?, ?, ?)
        '''
        ID = 1
        Query_tube = (ID,str(Nameinput.value),str(Professioninput.value),
                      str(Companyinput.value),str(Statusinput.value),birthDisplay.value)
        try:
            cursor.execute(Update_DB_query)
            print("Command in process")
            Display_Profile(e)
            db.commit()
        except sqlite3.Error as error:
            print(error)
        
        page.update()
    def Display_Edit_Profile(e):
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
                Birthday = obj[4]
            Nameinput.value = str(Name)
            Professioninput.value = str(Profession)
            Companyinput.value = str(Company)
            Statusinput.value = str(Status)
            Birthday_select_text.value = f'{Birthday}'
            db.commit()
        except sqlite3.Error as error:
            print(error)
        page.update()

    
    
    #--------------- BUILD FUNCTION ------------------------- 
    #Birthday Selection
    def Selected_page(e):
        for index, page_nav in enumerate(page_stack):
            page_nav.visible = True if index == AppBar.selected_index else False
            
            
        page.update()
    def Birthday_selection(e):
        Birthday_select_text.value = e.control.value.strftime('%Y-%m-%d')
        birthDisplay.value = Birthday_select_text.value
        print(birthDisplay.value)
        page.update()

    def Search_bar(e):
        Search.opacity = 0 if Search.opacity == 1 else 1
        Search.update()
        page.update()

    def Animate_TopBar(e):
        Greeting_banner.height = 200 if Greeting_banner.height == 130 else 130
        page.update()
    def Animate_TopBar_close(e):
        Greeting_banner.height = 130 if Greeting_banner.height == 200 else 200
        page.update()

    def Open_Search(e):
        SearchIcon.visible = False
        BackSearchIcon.visible = True
        Animate_TopBar(e)
        Search_bar(e)
        Search.visible = True
        page.update()

    def Close_Search(e):
        SearchIcon.visible = True
        BackSearchIcon.visible = False
        Search_bar(e)
        time.sleep(0.3)
        Animate_TopBar_close(e)
        Search.visible = False
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
        animation_ref_1.animate_scale=ft.animation.Animation(duration=500,curve="bounceOut")
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
        animation_ref_1.animate_scale=ft.animation.Animation(duration=500,curve="bounceOut")
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
        image_src="https://scontent-hkg1-1.xx.fbcdn.net/v/t39.30808-6/326753167_6249603558392243_3752875849790351645_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=127cfc&_nc_eui2=AeFQWfvDZ1bf0JLLs8qCoJbrWiUkN8epkqhaJSQ3x6mSqIU_Uu39JO9eqzjAxlmHOvYArXKoGP3DOGXeoUDIPEat&_nc_ohc=6KHydAzxh5gQ7kNvgFsZ3fm&_nc_ht=scontent-hkg1-1.xx&gid=AMugb3JbBHEA5km7u8Zxow1&oh=00_AYDACS3pJLBsxaDE5GUOtKio42HujUqinf8n53RWEtJj-A&oe=668ADAC6",
        bgcolor="grey",
        border=ft.border.BorderSide(5,"black"),
        border_radius=100,
        height=150,
        width=150,
        image_fit=ft.ImageFit.COVER

    )
    Editavt = ft.Container(
        image_src="https://scontent-hkg1-1.xx.fbcdn.net/v/t39.30808-6/326753167_6249603558392243_3752875849790351645_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=127cfc&_nc_eui2=AeFQWfvDZ1bf0JLLs8qCoJbrWiUkN8epkqhaJSQ3x6mSqIU_Uu39JO9eqzjAxlmHOvYArXKoGP3DOGXeoUDIPEat&_nc_ohc=6KHydAzxh5gQ7kNvgFsZ3fm&_nc_ht=scontent-hkg1-1.xx&gid=AMugb3JbBHEA5km7u8Zxow1&oh=00_AYDACS3pJLBsxaDE5GUOtKio42HujUqinf8n53RWEtJj-A&oe=668ADAC6",
        bgcolor="grey",
        border=ft.border.BorderSide(5,"black"),
        border_radius=100,
        height=150,
        width=150,
        image_fit=ft.ImageFit.COVER

    )
    Homepage_AVT = ft.Container(
        image_src="https://scontent-hkg1-1.xx.fbcdn.net/v/t39.30808-6/326753167_6249603558392243_3752875849790351645_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=127cfc&_nc_eui2=AeFQWfvDZ1bf0JLLs8qCoJbrWiUkN8epkqhaJSQ3x6mSqIU_Uu39JO9eqzjAxlmHOvYArXKoGP3DOGXeoUDIPEat&_nc_ohc=6KHydAzxh5gQ7kNvgFsZ3fm&_nc_ht=scontent-hkg1-1.xx&gid=AMugb3JbBHEA5km7u8Zxow1&oh=00_AYDACS3pJLBsxaDE5GUOtKio42HujUqinf8n53RWEtJj-A&oe=668ADAC6",
        bgcolor="grey",
        border=ft.border.BorderSide(1,"grey"),
        border_radius=100,
        height=30,
        width=30,
        image_fit=ft.ImageFit.COVER

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
                form,
                
            ]
        ),
        width=330,        
        height=490,
        bgcolor="white",
        border_radius=20,
        margin=ft.margin.only(top=10,left=3),
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
        width=330,
        height=490,
        bgcolor="white",
        border_radius=20,
        margin=ft.margin.only(top=10,left=3),
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
    
    
    #APP'S NAVIGATION

    #Set up Page List and Loop
    Search = ft.Container(
        ft.TextField(width=300,height=50,border_color="grey",hint_text="Search...",
            hint_style=ft.TextStyle(color="grey",size=15),
            text_size=15,border_radius=10,color="grey"
        ),
        animate_opacity=500,opacity=0,
        visible=False
    )
    #Type CupertinoNavigationBar
    #Custom Tabs
    SelectionTabs = ft.Tabs(
        selected_index=1,
        animation_duration=500,
        tabs=[
            ft.Tab(
                text="to do",
                icon="Book"
            ),
            ft.Tab(
                text="Schedule",
                icon="Schedule"
            ),
            ft.Tab(
                text="ChatAI",
                icon=ft.icons.CHAT
            ),
            ft.Tab(
                text="Profile",
                icon=ft.icons.ACCOUNT_BOX_ROUNDED
            )
        ],
        label_color=ft.colors.PINK_200,
        divider_color=ft.colors.PINK_50,
        scrollable=True,
        indicator_color="white",
        unselected_label_color="grey"  
    )


    ScheduleTabs = ft.Tabs(
        selected_index=1,
        animation_duration=500,
        tabs=[
            ft.Tab(
                text="Monday",
                
            ),
            ft.Tab(
                text="Tuesday",
                
            ),
            ft.Tab(
                text="Wednesday",
                
            ),
            ft.Tab(
                text="Thursday",
                
            ),
            ft.Tab(
                text="Friday",
                
            ),
            ft.Tab(
                text="Saturday",
                
            ),
            ft.Tab(
                text="Sunday",
                
            )
        ],
        label_color=ft.colors.PINK_200,
        divider_color=ft.colors.PINK_50,
        scrollable=True,
        indicator_color="white",
        unselected_label_color="grey",
         
    )
    #Create Button Actor
    SearchIcon = ft.IconButton(icon="search",icon_color="grey",on_click=Open_Search,visible=True)
    BackSearchIcon = ft.IconButton(icon="search",icon_color="grey",on_click=Close_Search,visible=False)
    #Custome Actor, Banner, Design for page_1
    Greeting_banner = ft.Container(
        ft.Column(
            [
                ft.Row(
                    [
                        
                        ft.IconButton(ft.icons.MENU,icon_color="grey",visible=True),
                        ft.Text("UpCase",color="grey",size=25,weight="bold"),
                        SearchIcon,
                        BackSearchIcon
                            
                    ],
                    alignment="spaceBetween",
                ),
                ft.Row(
                    [
                        Search,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                SelectionTabs
                
            ]
        ),
        border_radius=ft.border_radius.vertical(
            bottom=30
        ),
        bgcolor=ft.colors.PINK_50,
        width=400,
        height=130,
        padding=5,
        shadow= ft.BoxShadow(
            blur_radius=3,
            color="black",
            blur_style=ft.ShadowBlurStyle.OUTER
        ),
        animate=ft.animation.Animation(1000, ft.AnimationCurve.BOUNCE_OUT),
        
        
    )
    #UTILITIES

    #AI Tools
    AI_image = ft.Container(
        image_src="https://img.freepik.com/premium-photo/digital-world-online-shopping-via-phone-pink-phone-pink-background-ai-generated_744422-7299.jpg",
        height=150,
        width=230,
        border_radius=20,
        bgcolor="white",
        image_fit= ft.ImageFit.FILL
    )
    AI_utility = ft.Container(
        ft.Column(
            [
                AI_image,
                ft.Row(
                    [
                        ft.Text("AI Supporting",color="grey")
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ]
        ),
        height=250,
        width=250,
        border_radius=20,
        bgcolor="white",
        padding= ft.padding.only(left=10,top=10),
        margin=ft.margin.only(left=3),
        shadow= ft.BoxShadow(
            blur_radius=3,
            color="black",
            blur_style=ft.ShadowBlurStyle.OUTER
        )
    )
    #ToDo 
    ToDo_image = ft.Container(
        image_src="https://i.pinimg.com/736x/30/47/d7/3047d747871c7b5421137d644b7dbf04.jpg",
        height=150,
        width=230,
        border_radius=20,
        bgcolor=ft.colors.GREY_100,
        image_fit= ft.ImageFit.COVER
    )
    ToDo_utility = ft.Container(
        ft.Column(
            [
                ToDo_image,
                ft.Row(
                    [
                        ft.Text("ToDo List",color="grey")
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ]
        ),
        height=250,
        width=250,
        border_radius=20,
        bgcolor="white",
        padding= ft.padding.only(left=10,top=10),
        shadow= ft.BoxShadow(
            blur_radius=3,
            color="black",
            blur_style=ft.ShadowBlurStyle.OUTER
        )
    )
    #Note and Line up
    Note_image = ft.Container(
        image_src="https://c0.wallpaperflare.com/preview/356/153/277/adult-businessman-composition-desk.jpg",
        height=150,
        width=230,
        border_radius=20,
        bgcolor=ft.colors.GREY_100,
        image_fit= ft.ImageFit.COVER
    )

    Note_utility = ft.Container(
        ft.Column(
            [
                Note_image,
                ft.Row(
                    [
                        ft.Text("Note & Line",color="grey")
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ]
        ),
        height=250,
        width=250,
        border_radius=20,
        bgcolor="white",
        padding= ft.padding.only(left=10,top=10),
        
        shadow= ft.BoxShadow(
            blur_radius=3,
            color="black",
            blur_style=ft.ShadowBlurStyle.OUTER
        )
    )





    Header_main = ft.Container(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Utilities",color=ft.colors.WHITE,weight="bold",size=20)
                    ],
                    alignment=ft.MainAxisAlignment.START
                ),
                ft.Row(
                    [
                        AI_utility,
                        ToDo_utility,
                        Note_utility
                        
                    ],
                    scroll=ft.ScrollMode.ALWAYS,
                    
                    height=300
                )
            ]
        ),
        width=400,
        height=350,
        margin=ft.margin.only(top=10),
        # padding=5
        
       
    )




    #Schedule

    Schedule = ft.Container(
        ft.Column(
            [
                ScheduleTabs,
            ]
        ),
        height=300,
        width=400,
        bgcolor="white",
        shadow= ft.BoxShadow(
            blur_radius=3,
            color="black",
            blur_style=ft.ShadowBlurStyle.OUTER
        ),
        border_radius=20,
        padding=10

    )
    #Body main
    Body_main = ft.Container(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Schedule",color=ft.colors.WHITE,weight="bold",size=20)
                    ],
                    alignment=ft.MainAxisAlignment.START
                ),
                Schedule
            ]
        ),
        width=400,
        height=350,
        padding=5,
        
        
       
    )
    


    #Build up Page list

    
    page_1 = ft.Container(
        ft.Column(
            [
                
                Header_main,
                Body_main
                
            ],
            
            scroll=ft.ScrollMode.ALWAYS
        ),
        visible=True
    )
    page_2 = ft.Container(
        ft.Column(
            [
                
                
                
            ],
            scroll=ft.ScrollMode.ALWAYS
        ),
        
        visible=False
    )
    page_3 = ft.Container(
        ft.Column(
            [
                ft.Text("Help",size=30,color="white")
            ]
        ),
        visible=False
    )
    page_4 = ft.Container(
        
        ft.Column(
            [
                
                ft.Row(
                    controls=[
                        Profile,
                        EditProfile,
                        
                    ]
                ),
                ActionEvent,
            ],
            
            scroll=None
        ),
        width=500,
        visible=False,
        
       
    )


    page_stack = [
        page_1,
        page_2,
        page_3,
        page_4
    ]
    AppBar = ft.CupertinoNavigationBar(
        
        selected_index=0,
        on_change=Selected_page,
        bgcolor=ft.colors.WHITE,
        inactive_color=ft.colors.GREY,
        active_color=ft.colors.PINK_100,
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME, label="Home"),
            ft.NavigationDestination(icon=ft.icons.LIST, label="TODO"),
            ft.NavigationDestination(icon=ft.icons.HELP, label="Help"),
            ft.NavigationDestination(icon=ft.icons.ACCOUNT_BOX, label="Profile"),

        ],
        
        
    )

    #-----------------------------------------------------------------------
    page.overlay.append(DatePickUp)
    
    
    def route_change(e):
        page.views.clear
        page.views.append(
            View(
                "/HOME",
                [
                    Greeting_banner,
                    AppBar,
                    ft.Column(page_stack,scroll=True, expand=True)
                ],
                Display_Profile(e),
                Display_Edit_Profile(e),
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

    
    page.update()

if __name__ == "__main__":
    ft.app(target=main,assets_dir='assets')