import dash_bootstrap_components as dbc
from dash import html

def percent_input(label, input_id, value=None, min_value=0, max_value=100, step=0.1):
    return html.Div(
        [
            html.Label(
                label,
                style={
                    "fontSize": "15px",
                    "fontWeight": "500",
                    "marginBottom": "5px",
                }
            ),
            dbc.InputGroup(
                [
                    dbc.Input(
                        id=input_id,
                        type="number",
                        value=value,
                        min=min_value,
                        max=max_value,
                        step=step,
                        style={"width": "100%"}
                    ),
                    dbc.InputGroupText("%"),
                ],
                style={"display": "flex"},
            ),
        ],
        style={
            "marginBottom": "20px",
            "display": "flex",
            "flexDirection": "column",
        },
    )

