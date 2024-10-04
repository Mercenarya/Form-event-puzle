import pyrebase
import flet as ft
from flet import View
import os



path_dir = os.path.dirname(os.path.abspath(__file__))

fb = {
    'apiKey': "AIzaSyCe3AOYttBOSqy3WJU3tsYpcwYy4r6j_0s",
    'authDomain': "pushgram-mobile.firebaseapp.com",
    'projectId': "pushgram-mobile",
    'storageBucket': "pushgram-mobile.appspot.com",
    'messagingSenderId': "605706942308",
    'appId': "1:605706942308:web:80385154abe5fb64882c71",
    'measurementId': "G-LBXDNVD3T3",
    "databaseURL": "https://pushgram-mobile-default-rtdb.firebaseio.com/"
}

_fbase_init = pyrebase.initialize_app(fb)
_fbase_authoriztion = _fbase_init.auth()
storage = _fbase_init.storage()
database_fb = _fbase_init.database()

'''
Create sign in page with firebase authentication
(gmail and Phone number)

'''
class SigninPage(ft.Column):
    def __init__(self, temp_btn_signup):
        super().__init__()
        self.gmail = ft.TextField(width=400,label="Gmail")
        self.password = ft.TextField(width=400,can_reveal_password=True,password=True,label="Password")
        self.temp_btn_signup = temp_btn_signup

        #Dialog with customize
        self.contentDialog = ft.AlertDialog(
            title=ft.Text(),
            content=ft.Text(),
            actions=[
                
            ],
        )


        
        self.__page_layout = ft.Container(
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Text("Dicussion Event",size=30,weight="bold"),
                                ],
                                width=400,
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            self.gmail,
                            self.password,
                            ft.ElevatedButton(
                                "Claim Event with @Puzlevn",
                                bgcolor="black",
                                color="white",
                                width=400,
                                on_click=self.Signin_Progress,
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
                            ),
                            self.temp_btn_signup
                        ]
                    )
                    
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            margin=ft.margin.only(top=100,left=500),
            # margin=100,
            padding=50,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.colors.GREY,
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),
            height=500,
            width=550
            
        )
        self.controls = [self.__page_layout,self.contentDialog]

        '''
        Sign-in logical-processing
        expect with completed and failed cases
        (try - except logically)
        '''
    
    
        

    def Signin_Progress(self, e):
        try:
            ''' if user have verified their account successfully'''
            sign_in = _fbase_authoriztion.sign_in_with_email_and_password(email=self.gmail.value,password=self.password.value)
            #Display Dialog with successfully
            self.contentDialog.title = ft.Text("Sign in Completed")
            self.contentDialog.content = ft.Text(f"sign in as {self.gmail.value}")
            self.contentDialog.actions = [
                ft.TextButton("Continue",on_click=self.Change_View_HP)
            ]
            self.Open_dialog(e)

        except :
            ''' failed sign in in this stage'''
            #Display Dialog with failed
            self.contentDialog.title = ft.Text("Sign in failed")
            self.contentDialog.content = ft.Text("Wrong Gmail or password, try again.")
            self.contentDialog.actions = [
                ft.TextButton("Ok",on_click=self.Close_Dialog)
            ]
            self.Open_dialog(e)
        self.update()
    

    '''Custom dialog interact'''
    
    def Open_dialog(self, e):
        self.contentDialog.open = True
        self.update()

    def Close_Dialog(self, e):
        self.contentDialog.open = False
        self.update()

    def Change_View_HP(self, e):
        try:
            
            try:
                # main_screen(page=self.page)

                self.Close_Dialog(e)
                self.__page_layout.visible = False
                
            except Exception as error:
                print(error)
            
        except Exception as error:
            self.contentDialog.title = ft.Text("Error")
            self.contentDialog.content = ft.Text(f"{error}")
            self.contentDialog.actions = [
                ft.TextButton("Ok",on_click=self.Close_Dialog)
            ]
            self.Open_dialog(e)
        self.update()
    


'''
Routing - change course and delivery request from user
to Sign up page
'''
"Temp_btn is a oriented element used to add routed button from outside"
''''''
class SignupPage(ft.Column):
    def __init__(self, temp_btn):
        super().__init__()
        self.gmail = ft.TextField(width=400,label="Create Gmail")
        self.password = ft.TextField(width=400,can_reveal_password=True,password=True,label="Password")
        self.password_review = ft.TextField(width=400,can_reveal_password=True,password=True,label="Password")
        self.temp_btn = temp_btn
        #Dialog with customize
        self.contentDialog = ft.AlertDialog(
            title=ft.Text(),
            content=ft.Text(),
            actions=[
                
            ],
        )


        
        self.__page_layout = ft.Container(
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Text("Sign up",size=30,weight="bold"),
                                ],
                                width=400,
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            self.gmail,
                            self.password,
                            ft.ElevatedButton(
                                "Sign up",
                                bgcolor="blue",
                                color="white",
                                width=400,
                                on_click=self.Signup_Progress,
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
                            ),
                            self.temp_btn
                        ]
                    )
                    
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            margin=ft.margin.only(top=100,left=500),
            # margin=100,
            padding=50,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.colors.GREY,
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),
            height=500,
            width=550
            
        )
        self.controls = [self.__page_layout,self.contentDialog]

    def Signup_Progress(self, e):
        try:
            ''' if user have signed up their account successfully'''
            sign_up = _fbase_authoriztion.create_user_with_email_and_password(email=self.gmail.value, password=self.password.value)
            self.contentDialog.title = ft.Text("Sign up Completed")
            self.contentDialog.content = ft.Text("Your Account have been activated")
            self.contentDialog.actions = [
                ft.TextButton("Ok",on_click=self.Close_Dialog)
            ]
            self.Open_dialog(e)
        except :
            ''' failed sign up in this stage'''
            self.contentDialog.title = ft.Text("Sign up failed")
            self.contentDialog.content = ft.Text("Gmail have already exists")
            self.contentDialog.actions = [
                ft.TextButton("Ok",on_click=self.Close_Dialog)
            ]
            self.Open_dialog(e)
        self.update()
    
    def Open_dialog(self, e):
        self.contentDialog.open = True
        self.update()

    def Close_Dialog(self, e):
        self.contentDialog.open = False
        self.update()
    

def main(page: ft.Page):

    '''
    Custom outside elements
    - Signin btn
    - go to sign in
    - go to sign up
    '''
    

    Signupbtn = ft.ElevatedButton(
        "Go to Sign up",
        bgcolor="blue",
        color="white",
        width=400,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),
        on_click= lambda _:page.go("/Signup")
    )

    Signinbtn = ft.ElevatedButton(
        "Go to Sign in",
        bgcolor="black",
        color="white",
        width=400,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),
        on_click= lambda _:page.go("/Login")
    )

    '''
    Route changing and View
    included Sign up and sign in when
    user is interacting with button
    '''
   

 

    def route_change(e):
        page.views.clear
        page.views.append(
            View(
                "/Login",
                [           
                    SigninPage(Signupbtn)
                ],
            ),
                
        ),
        page.theme_mode = ft.ThemeMode.LIGHT
        if page.route == "/Signup":
            page.views.append(
                View(
                    "/Signup",
                    [
                        SignupPage(Signinbtn)
                    ],
                    
                ),
               
            ),


        page.theme_mode = ft.ThemeMode.LIGHT
        page.update()
    
    def view_pop(View):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    

    '''
    Routing page with function and logics
    '''
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    page.padding = 0
    page.update()

if __name__ == "__main__":
    ft.app(target=main,view=ft.AppView.WEB_BROWSER)
