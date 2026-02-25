from dash import html, dcc
from components.sidebar import sidebar
from components.card import kpi_card
from components.card_box import card_box
from components.area_chart import area_projection_chart
from components.button import button
from components.grid import grid
import dash_ag_grid as dag
import pandas as pd
import numpy as np

home_layout = html.Div(
    className="layout",
    children=[
        sidebar,
        # Right side container
        html.Div(
            className="content",
            children=[
                # Cards container
                html.Div(
                    [
                        kpi_card("Total Capital", "1,250,000€", "kpi-networth"),
                        kpi_card("Total Net Savings", "1,250,000€", "kpi-savings"),
                        kpi_card("Projected Portfolio", "250,000€", "kpi-funds"),
                        kpi_card("Financial Freedom", "45", "kpi-time"),
                    ],
                    style={
                        "display": "flex",
                        "flexWrap": "wrap",
                        "gap": "20px",
                    },
                ),

                # Card Box
                html.Div(
                    card_box(
                        title="TOTAL CONTRIBUTED CAPITAL PROJECTION",
                        header_button=button(
                                    [
                                        html.I(
                                            className="fa-solid fa-file-excel",
                                            style={"fontSize": "20px", "color": "#217346","marginRight": "8px", "margin-left":"auto"},
                                        ),
                                        "",
                                    ],
                                    id="csv-download",
                                    color="transparent",
                                ),
                        children = [
                            html.Div(
                                [
                                dcc.Graph(
                                    id="pie-chart",
                                    config={"displayModeBar": False},
                                    style={
                                        "height": "335px",
                                        "width": "30%",
                                    },
                                ),
                                dcc.Graph(
                                    id="projection-chart",
                                    config={"displayModeBar": False},
                                    style={
                                        "height": "335px", 
                                        "width": "70%",
                                        },
                                ),
                                ],
                            style={"marginBottom": "15px", "display":"flex", "alignItems": "stretch", "minHeight": "335px"},
                            ),
                            html.Div(
                                [
                                    html.Div(
                                        id="grid-container",
                                        children=grid(),
                                        style={"width": "100%"}
                                    ),
                                #kpi_card("Conservative", "1,250,000€", "kpi-conservartive",style={"boxShadow": "none", "border": "none"}),
                                #kpi_card("Optimistic", "1,250,000€", "kpi-optimistic",style={"boxShadow": "none", "border": "none"}),
                                #kpi_card("Agressive", "1,250,000€", "kpi-agressive",style={"boxShadow": "none", "border": "none"}),
                                #kpi_card("Total Time", "0", "kpi-freedom",style={"boxShadow": "none", "border": "none"}),
                                ],
                                style={
                                    "display": "flex",
                                    "flexWrap": "wrap",
                                    "gap": "15px",
                                    "border": "none",
                                    "boxShadow": "none",
                                },
                            ),
                        ], #here will go the area line chart
                    ),
                ),

                # Footer text
                html.Div(
                    "Made by Clavert Consulting",
                    style={
                        "fontSize": "12px",
                        "color": "grey",
                        "marginTop": "20px",
                        "textAlign": "center",
                        "margin-bottom":"50px"
                    }
                )
            ],
            style={
                "width": "85%",
                "padding": "20px",
                "display": "flex",
                "flexDirection": "column",
                "overflowY": "auto",
                "flex": "1",
            }
        )
    ],
    style={"display": "flex","height": "100vh"}
)
