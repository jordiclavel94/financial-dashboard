import dash_bootstrap_components as dbc

def button (title,id, color="", className="", padding=""):
    return dbc.Button(
        title, 
        id = id,
        color=color, 
        className=className,
        style={
            "fontSize": "15px",
            "padding": padding,
            "backgroundColor":color,
            "borderRadius":"12px",
            "borderWidth": "0",
            "cursor": "pointer",         # Shows hand on hover
            "transition": "all 0.2s",
            "color":"white"
        },
        )