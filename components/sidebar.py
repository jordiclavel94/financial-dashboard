from dash import html, dcc
from components.number_input import number_input
from components.percent_input import percent_input
from components.button import button

sidebar = html.Div(
    className="sidebar",
        children=[
            html.Div("CALCULATION PARAMETERS:", className="sidebar-title"),
            number_input("Current Age", "current-age", 30, 1, 100, 1),
            number_input("Retirement Age", "retirement-age", 65, 1, 100, 1),
            number_input("Monthly Net Salary (€)", "monthly-salary", 3000, 100, 10000, 100),
            number_input("Monthly Investment (€)", "monthly-investment", 500, 100, 10000, 50),
            number_input("Monthly Expenses (€)", "monthly-expenses", 1000, 100, 10000, 100),
            number_input("Initial Investment (€)", "initial-investment", 0, 0, 1000000, 100),
            number_input("Investment Rate (%)", "anual-return", 2, 1, 100, 1),
            number_input("Variance Rate (%)", "anual-variance", 2, 1, 100, 1),
            html.Div(
                button(
                    [
                        html.I(
                            className="fa-solid fa-play",
                            style={
                                "fontSize": "15px",
                                "marginRight": "8px",
                                "color": "white"
                            },
                        ),
                        "Run Simulation",
                    ],
                    id="run-simulation",
                    color="#0d6efd",
                    padding="10px 20px",
                    ), 
                style ={
                    "display":"flex",
                    "justify-content":"center"
                    }
                )      
        ],
        style={
        "width": "15%",
        "minHeight": "100vh",
        }
    )
