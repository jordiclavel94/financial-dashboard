import dash_bootstrap_components as dbc
from dash import html

def number_input(label, input_id, value=None, min_value=None, max_value=None, step=None):
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
            dbc.Input(
                id=input_id,
                type="number",
                value=value,
                min=min_value,
                max=max_value,
                step=step,
            ),
        ],
        style={
            "marginBottom": "20px",
            "display": "flex",
            "flexDirection": "column",
        },
    )