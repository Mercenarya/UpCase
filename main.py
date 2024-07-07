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

class Task(ft.Column):
    
    def __init__(self, name_task, delete_task):
        super().__init__()
        self.name_task = name_task
        self.delete_task = delete_task
        self.Task_value =ft.Text(value=self.name_task,color="white")
        
        self.display_task =  ft.Container(
                ft.Row(
                    controls=[
                            ft.Checkbox(check_color="white"),
                            ft.Container(
                                self.Task_value,
                                width=200,
                                height=20
                            ),
                            ft.IconButton(ft.icons.DELETE,icon_color="red",on_click=self.Deletete_clicked)
                        ]
                    ),
                padding=ft.padding.only(left=10),
                width=400,
                height=50,
                border=ft.border.all(1,"orange"),
                bgcolor="orange"
            )
        self.controls = [self.display_task]
    def Deletete_clicked(self, e):
        self.delete_task(self)

class TodoApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.Task_Field = ft.TextField(width=270,border_color="white",hint_text="Task...",
                              hint_style=ft.TextStyle(color="grey"),color="white")
        
        self.Todo_list = ft.Column(
            [
                
            ],
            scroll=ft.ScrollMode.ALWAYS,
            height=400,
            width=400
        )
       
        self.controls = [
            ft.Row(
                controls=[
                    self.Task_Field,
                    ft.FloatingActionButton(
                        icon=ft.icons.ADD, on_click=self.add
                    )
                ]
            ),
            self.Todo_list
        ]

    def add(self, e):
        task = Task(self.Task_Field.value, self.Delete)
        self.Todo_list.controls.append(task)
        self.update()

    def Delete(self, task):
        self.Todo_list.controls.remove(task)
        self.update()
    

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
    #To do Feartures 

    



    #Birthday Selection
    def Tabs_TopBar(e):
        OpenBar.visible = False
        CloseBar.visible =True
        Greeting_banner.height = 500 if Greeting_banner.height == 50 else 50
        page.update()
    def Tabs_TopBar_close(e):
        OpenBar.visible = True
        CloseBar.visible = False
        Greeting_banner.height = 50 if Greeting_banner.height == 500 else 500
        page.update()

    def Invisible_banner(e):
        if AppBar.selected_index == page_4:
            Greeting_banner.visible = False
        else:
            Greeting_banner.visible = True
        page.update()    
    def Selected_page(e):
        
        for index, page_nav in enumerate(page_stack):
            page_nav.visible = True if index == AppBar.selected_index else False
        
        page.update()
    def Selected_tabs(e):
        for index, page_nav in enumerate(page_tabs):
            page_nav.visible = True if index == SelectionTabs.selected_index else False
        page.update()

    def Birthday_selection(e):
        Birthday_select_text.value = e.control.value.strftime('%Y-%m-%d')
        birthDisplay.value = Birthday_select_text.value
        print(birthDisplay.value)
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
        Profile.update()
        EditProfile.update()
        page.update()

    def ActionBacktoProfile(e):
        Profile.offset = ft.transform.Offset(0,0)
        EditProfile.offset = ft.transform.Offset(2,0)
        NextAction.visible = True
        BackAction.visible = False
        ChangeSwitched.value = "Profile"
        Profile.update()
        EditProfile.update()
        page.update()
    
   
    #--------------- CUSTOMIZE DESIGN VIEW -----------------

    






    '''
        PROFILE PAGE IS THE LAST SELECTION FROM CUPERTINO BAR BELOW
        PROFILE WITH EDIT AND DISPLAY YOUR PERSONAL INFORMATION 
    '''

    #Text Actor 
    NameDisplay = ft.Text("Tran Hoang Minh",color="grey",weight="bold")
    professionDisplay = ft.Text("Mobile Developer",color="grey",weight="bold")
    companyDisplay = ft.Text("DVT Group",color="grey",weight="bold")
    statusDisplay = ft.Text("On work",color="grey",weight="bold")
    birthDisplay = ft.Text("11/10/1997",color="grey",weight="bold")
    
    ChangeSwitched = ft.Text("Profile",size=30,color="white")
    #Animation
    
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
    SaveProfile = ft.ElevatedButton("Save",color="white",bgcolor=ft.colors.GREY_500,on_click=Update_Profile)
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
        image_src="C:/pen.png",
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
        bgcolor=ft.colors.GREY_100,
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
        bgcolor=ft.colors.GREY_100,
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
                
                ChangeSwitched,
                NextAction,
                BackAction
            ],
            alignment=ft.MainAxisAlignment.END
        )
    )
    
    #-----------------------------------
    '''
        TO DO FEATURE IN UPCASE WITH HELP BEING SCHEDULED ALL 
        TASKS TO DO AND PLANS
    '''
    
    

    

    

   
    
    



   
    #-----------------------------------
    '''
        HOMEPAGE IN UPCASE WITH ALL UTITLITIES
        INITIAL VIEW FROM CUPERTINOBAR ROUTE BELOW (HOME)
    '''
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

    #ToDo Feature
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
        label_color=ft.colors.BLACK,
        divider_color=ft.colors.GREY,
        scrollable=True,
        indicator_color="grey",
        unselected_label_color="grey",
         
    )
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
                TodoApp()
            ],
            height=500
        ),
        visible=False
    )
    # page_2 = TodoApp()
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
    #Set up Page List and Loop
    
   
    #Build up Page list
    Todo_tabs_notification = ft.Column(
        [

        ]
    )
    page_stack = [
        page_1,
        page_2,
        page_3,
        page_4
    ]
    #Build Tabs Selection 
    tabs_1 = ft.Container(
        ft.Column(
            [
                ft.Text("Home",size=30,color="white"),
                
                
            ],
            scroll=ft.ScrollMode.ALWAYS
        ),
        visible=True
    )
    tabs_2 = ft.Container(
        ft.Column(
            [
                ft.Column(
                    [
                        ft.Text("Todo",size=30,color="white"),
                    ],
                    
                ),
                Todo_tabs_notification
                
            ],
            scroll=ft.ScrollMode.ALWAYS
        ),
        visible=True,
    )
    tabs_3 = ft.Container(
        ft.Column(
            [
                ft.Text("Schedule",size=30,color="white")
            ],
            scroll=ft.ScrollMode.ALWAYS
        ),
        visible=True
    )
    tabs_4 = ft.Container(
        ft.Column(
            [
                ft.Text("Chat AI",size=30,color="white")
            ],
            scroll=ft.ScrollMode.ALWAYS
        ),
        visible=True
       
    )
    tabs_5 = ft.Container(
        ft.Column(
            [
                ft.Text("Profile",size=30,color="white")
            ],
            scroll=ft.ScrollMode.ALWAYS
        ),
        width=500,
        visible=True,
       
    )


    page_tabs = [
        tabs_1,
        tabs_2,
        tabs_3,
        tabs_4,
        tabs_5
    ]
    #Custom Tabs
    SelectionTabs = ft.Tabs(
        on_change=Selected_tabs,
        selected_index=0,
        animation_duration=500,
        tabs=[
            ft.Tab(
                text="Home",
                icon="Home",
                content=tabs_1
            ),
            ft.Tab(
                text="to do",
                icon="Book",
                content=tabs_2
            ),
            ft.Tab(
                text="Schedule",
                icon="Schedule",
                content=tabs_3
            ),
            ft.Tab(
                text="ChatAI",
                icon=ft.icons.CHAT,
                content=tabs_4
            ),
            ft.Tab(
                text="Profile",
                icon=ft.icons.ACCOUNT_BOX_ROUNDED,
                content=tabs_5
                
            ),
            
        ],
        expand=1,
        label_color=ft.colors.WHITE,
        divider_color=ft.colors.ORANGE,
        scrollable=True,
        indicator_color="white",
        unselected_label_color="White"  
    )


    Search = ft.Container(
        ft.TextField(width=300,height=50,border_color="white",hint_text="Search...",
            hint_style=ft.TextStyle(color="white",size=15),
            text_size=15,border_radius=10,color="white"
        ),

        
    )
    
    #Create Button Actor
    OpenBar = ft.Container(width=100,height=10,bgcolor="grey",on_click=Tabs_TopBar,visible=True)
    CloseBar = ft.Container(width=100,height=10,bgcolor="grey",on_click=Tabs_TopBar_close,visible=False)

    Menu = ft.IconButton(ft.icons.MENU,icon_color="white",on_click=None,visible=True)
    SearchIcon = ft.IconButton(icon="search",icon_color="white",on_click=None,visible=True)
    #Custome Actor, Banner, Design for page_1
    Greeting_banner = ft.Container(
        ft.Column(
            [
                ft.Row(
                    [
                        
                        Menu,
                        ft.Text("UpCase",color="white",size=25,weight="bold"),
                        SearchIcon,
                        
                            
                    ],
                    alignment="spaceBetween",
                ),
                ft.Row(
                    [
                        Search,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                SelectionTabs,
                
            ]
        ),
        border_radius=ft.border_radius.vertical(
            bottom=25
        ),
        bgcolor="Orange",
        width=400,
        height=50,
        padding=10,
        shadow= ft.BoxShadow(
            blur_radius=3,
            color="black",
            blur_style=ft.ShadowBlurStyle.OUTER
        ),
        animate=ft.animation.Animation(1000, ft.AnimationCurve.BOUNCE_OUT),
        
        
    )
    
    


    
    
    #APP'S NAVIGATION
    #Type CupertinoNavigationBar
    AppBar = ft.CupertinoNavigationBar(
        
        selected_index=0,
        on_change=Selected_page,
        bgcolor=ft.colors.BLACK,
        inactive_color=ft.colors.GREY,
        active_color=ft.colors.ORANGE,
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
                    ft.Row(
                        [
                            OpenBar,
                            CloseBar
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    AppBar,
                    ft.Column(page_stack,scroll=True, expand=True)
                ],
                Display_Profile(e),
                Display_Edit_Profile(e),
                Invisible_banner(e),
                bgcolor="Black"
            )
        )
        if page.route == "/Profile":
            pass
        
        page.update()
    def view_pop(View):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    page.window_width =380
    page.window_resizable = False
    page.update()

if __name__ == "__main__":
    ft.app(target=main,assets_dir='assets')