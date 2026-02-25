from dash import html, Dash, dcc, no_update
from dash import Input, Output, callback, State
from components.navbar import navbar
from pages.home import home_layout
from components.area_chart import area_projection_chart
from components.pie_chart import pie_chart
from components.grid import grid
import pandas as pd
import numpy as np
import math

external_stylesheets = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div(
    [
    navbar,
    html.Div(home_layout),
    dcc.Store(id="grid-data-store"),
    dcc.Download(id="download-csv"),
    ]
)

@app.callback(
    Output("kpi-networth","children"),
    Output("kpi-savings","children"),
    Output("kpi-funds","children"),
    Output("kpi-time","children"),
    #Output("kpi-conservartive","children"),
    #Output("kpi-optimistic","children"),
    #Output("kpi-agressive","children"),
    #Output("kpi-freedom","children"),
    Output("pie-chart", "figure"),
    Output("projection-chart", "figure"),
    Output("grid-container","children"),
    Output("grid-data-store","data"),
    Input("run-simulation","n_clicks"),
    State("current-age","value"),
    State("retirement-age","value"),
    State("monthly-salary","value"),
    State("monthly-investment","value"),
    State("monthly-expenses","value"),
    State("anual-return","value"),
    State("anual-variance","value"),
)

def update_simulation(n_clicks, age, retirement_age, salary, investment, expenses, rate, variance):
    if not n_clicks:
        return "0€", "0€", "0€", "0", {}, {}, None, {}
    
    if None in (age, retirement_age, salary, investment, expenses, rate, variance):
        return "—", "—", "—", "—", {}, {}, None, {}
    
    years = retirement_age- age
    months = years*12
    r = rate/100
    o = (rate + variance) / 100
    a = (rate + variance*2) / 100

    # ----- KPI Cards Totals -----
    total_invested = investment*months
    total_saved = (salary-expenses-investment)*months
    projected_networth = total_saved + total_invested

    # ----- Build Yearly Projection -----
    x_years = np.arange(0, years + 1)

    yearly_investment = investment * 12
    yearly_savings = (salary - expenses - investment) * 12

    #portfolio_value = yearly_investment * x_years
    portfolio_value = (yearly_investment / 12) * (((1 + r/12)**(x_years*12) - 1) / (r/12))
    total_savings = yearly_savings * x_years
    total_contributed = portfolio_value + total_savings

    df = pd.DataFrame({
    "Year": x_years,
    "Total Capital Contributed (€)": total_contributed,
    "Total Net Savings (€)": total_savings,
    "Projected Portfolio (€)": portfolio_value,
    })

    df = df[df["Year"] != 0].round(0).astype(int)

    fig = area_projection_chart(df)

    # ----- Build Scenarios KPIs -----
    conservative = investment * (((1 + r/12)**months - 1) / (r/12))
    optimistic = investment * (((1 + o/12)**months - 1) / (o/12))
    agressive = investment * (((1 + a/12)**months - 1) / (a/12))
    projected_networth = total_saved + conservative

    # ----- Pie Chart (%) -----
    pie_df = pd.DataFrame({
    "Category": ["Total Net Savings", "Total Projected Portfolio"],
    "Amount": [total_saved, conservative]
    })

    pie_fig = pie_chart(pie_df)

    # ----- Financial Freedom -----
    i = r / 12
    target = expenses*12/r
    n = np.log(1 + i * (target) / investment) / np.log(1 + i)
    freedom_years = math.ceil(n / 12)

    df_grid = df.copy()
    df_grid["Financial Freedom"] = ["Yes" if pv >= target else "No" for pv in df_grid["Projected Portfolio (€)"]]

    return (
        f"{projected_networth:,.0f} €",
        f"{total_saved:,.0f} €",
        f"{conservative:,.0f} €",
        f"{freedom_years} years",
        #f"{conservative:,.0f} €",
        #f"{optimistic:,.0f} €",
        #f"{agressive:,.0f} €",
        #f"{years} years",
        pie_fig,
        fig,
        grid(df_grid),
        df_grid.to_dict("records")
    )

@app.callback(
    Output("download-csv", "data"),
    Input("csv-download", "n_clicks"),
    State("grid-data-store", "data"),
    prevent_initial_call=True
)
def download_csv(n_clicks, data):
    if not data:
        return no_update
    df_to_download = pd.DataFrame(data)
    return dcc.send_data_frame(df_to_download.to_excel, "simulation_data.xlsx", index=False, sheet_name="Simulation")

if __name__ == "__main__":
    app.run(debug=True)
