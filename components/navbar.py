from dash import html, dcc

navbar = html.Div(
    className = "navbar",
        children=[
            html.Div(
                "Personal Finance Simulator",
                className="navbar-brand"
            ),
            html.Div(
                className="navbar-links",
                children=[
                    #dcc.Link("Home", href="/", className="nav-link"),
                    html.I(
                        className="fa-solid fa-bars", 
                        style={"font-size":"20px","cursor":"pointer", "color":"white"}
                        ),
                    dcc.Link("Dashboard", href="/dashboard", className="nav-link"),
                ]
            ),
            html.Div(
                className='navbar-icons',
                children= [
                    html.I(
                        className="fa-solid fa-user", 
                        style={"font-size":"20px","cursor":"pointer", "color":"white"}
                        ),
                    html.I(
                        className="fa-solid fa-gear", 
                        style={"font-size":"20px","cursor":"pointer", "color":"white"}
                        ),
                    html.I(
                        className="fa-solid fa-circle-info",
                        style={"font-size":"20px","cursor":"pointer", "color":"white"}
                        ),
                ],
                style ={
                    "margin-left":"auto"
                },
            ),
        ],
    )