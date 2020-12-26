from ipywidgets import widgets, interact, interact_manual, TwoByTwoLayout
from IPython.display import IFrame, clear_output
from wikidataintegrator import wdi_login

class wikidata_login(object):
    def __init__(self):
        ## Login panel
        ### Label
        wikidata = widgets.HTML(value="<H2>Login to Wikidata</H2>")

        ### Username
        username_textbox = widgets.Text(
            value="",
            description="Username",
        )
        ## Password
        password_textbox = widgets.Password(description='Password:')
        ## Button
        loginbutton = widgets.Button(description="login", icon='sign-in-alt')
        ## Login as
        loginlabel = widgets.Label(value="Please login to Wikidata first")

        file = open("img/wikidata.png", "rb")
        image = file.read()
        logo = widgets.Image(
            value=image,
            format='png',
            width=250,
        )

        @loginbutton.on_click
        def wdlogin(b):
            login = wdi_login.WDLogin(username_textbox.value, password_textbox.value)
            creds = login.generate_edit_credentials()
            koekjes = creds.get_dict()
            loginlabel.value = "Logged in to Wikidata as User: " + koekjes["wikidatawikiUserName"]
            b.login = login

        loginPane = widgets.VBox(layout={'border': '1px solid black'},
                                 children=[wikidata, username_textbox, password_textbox, loginbutton, loginlabel])
        self.widget = TwoByTwoLayout(top_left=logo,
                                bottom_right=loginPane)
        #self.widget = widgets.HBox(children=[loginPane, logo])
        self.login = loginbutton

class biodiversity_tabs(object):
    tab = widgets.Tab()
    tab.children = [widgets.Text(), widgets.Text()]
    tab.titles = ["iNaturalist", "Wikidata"]