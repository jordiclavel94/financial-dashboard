from dash import html

def kpi_card(title, value, value_id, style=None):
    return html.Div(
        style = {
            "background":"white",
            "borderRadius":"12px",
            "padding":"10px 15px",
            "box-shadow":"0 2px 6px rgba(59,130,246,0.15)",
            "flex":"1",
            "minWidth":"236px",
            "box-sizing":"border-box",
            "height":"75px",
            "text-align": "center",
            "transition": "all 0.3s ease-in-out",
            "cursor": "pointer",
            **(style or {}),
        },
        children = [
            html.Div(
                title,
                style = {
                    "font-size":"14px",
                    "color":"#6B7280",
                    "marginBottom":"5px",
                    "textTransform":"uppercase",
                    "letterSpacing":"0.5px",
                },
            ),
            html.Div(
                value,
                id = value_id,
                style = {
                    "font-size":"28px",
                    "color":"#111827",
                    "fontweight":"600",
                },
            ),
        ],
    )