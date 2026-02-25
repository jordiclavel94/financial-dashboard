from dash import html, dcc

def card_box(title, children, header_button=None):
    return html.Div(
        style = {
            "background":"white",
            "borderRadius":"12px",
            "box-shadow":"0 2px 6px rgba(0,0,0,0.08)",
            "border":"1px solid #E5E7EB",
            "width":"100%",
            "display":"flex",
            "flex":"1",
            "overflow":"hidden",
            "margin-top":"20px",
            "flexDirection": "column",
        },
        children = [
            # Header
            html.Div(
                style = {
                    "background":"#ACBBC5",
                    "padding":"10px 20px",
                    "display":"flex",
                    "justify-content":"center",
                    "font-weight":"bold",
                    "alignItems":"center",
                    "gap":"20px"
                },
                children = [
                    html.Div(
                        title,
                        style = {
                            "font-size" : "15px",
                        },
                    ),
                    header_button if header_button else None,
                ],
            ),
            # Body
            html.Div(
                style = {
                    "padding":"10px",
                    "min-height": "300px",
                    "overflow": "auto",
                },
                children = children,
            ),
        ],
    )