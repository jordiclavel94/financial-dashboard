from dash import Dash, html
import dash_ag_grid as dag
import pandas as pd

DEFAULT_COLUMNS = [
    "Year",
    "Total Capital Contributed (€)",
    "Total Net Savings (€)",
    "Projected Portfolio (€)",
    "Financial Freedom"
]

def grid(df=None, columns=None, empty_rows=3):
    if df is None or df.empty:
        df = pd.DataFrame([{col: "" for col in DEFAULT_COLUMNS} for _ in range(empty_rows)])

    # If no columns are provided, use df's columns
    if columns is None:
        columns = df.columns.tolist()

    # Convert DataFrame to list of dicts for AgGrid
    row_data = df.to_dict("records")

    columnDefs = [
        {
            "headerName": col,
            "field": col,
            "sortable": True,
            "resizable": True,
            "wrapText": True,
            "minWidth": 230,
            "headerClass": "ag-center-header",
            "cellClass": "ag-center-cell",
        }
        for col in columns
    ]

    grid = dag.AgGrid(
        id="table-grid",
        rowData=row_data,
        columnDefs=columnDefs,
        dashGridOptions={
            "pagination": True,
            "paginationPageSize": 50, 
            "rowHeight": 35,
            "headerHeight": 40,
            "defaultColDef": {
                "flex": 1,       # makes all columns stretch evenly
                "minWidth": 230, # ensures minimum width
            },
            "domLayout": "normal"  # optional: grid height adjusts to content
        },
        style={"width": "100%", "minheight": "100px", "height": "320px"},
    )

    return grid