import plotly.graph_objects as go

def area_projection_chart(df):

    fig = go.Figure()

    # --- Projected Portfolio Value ---
    fig.add_trace(
        go.Scatter(
            x=df["Year"],
            y=df["Projected Portfolio (€)"],
            mode="lines+markers",
            name="Projected Portfolio (€)",
            fill="tozeroy",
            line=dict(width=2, color="#3B82F6"),
            marker=dict(color="#3B82F6"),
            legendrank=1,
        )
    )

    # --- Total Net Savings ---
    fig.add_trace(
        go.Scatter(
            x=df["Year"],
            y=df["Total Net Savings (€)"],
            mode="lines+markers",
            name="Total Net Savings (€)",
            fill="tonexty",
            line=dict(width=2, color="#2563EB"),
            marker=dict(color="#2563EB"),
            legendrank=2,
        )
    )

    # --- Total Capital Contributed ---
    fig.add_trace(
        go.Scatter(
            x=df["Year"],
            y=df["Total Capital Contributed (€)"],
            mode="lines+markers",
            name="Total Capital Contributed (€)",
            fill="tonexty",
            line=dict(width=2, color="#1F3A8A"),
            marker=dict(color="#1F3A8A"),
            legendrank=3,
        )
    )

    fig.update_layout(
        font=dict(family="Inter, sans-serif"),
        template="plotly_white",
        xaxis_title="Years",
        yaxis_title="Amount (€)",
        hovermode="x unified",
        legend=dict(
            orientation="h",
            y=1.02,
            yanchor="bottom",
            xanchor="center",
            x=0.5
        ),
        margin=dict(l=20, r=20, t=0, b=20),
    )

    # Stable Y-axis
    y_max = df[
        [
            "Total Capital Contributed (€)",
            "Total Net Savings (€)",
            "Projected Portfolio (€)"
        ]
    ].values.max()

    y_max *= 1.05

    fig.update_yaxes(
        tickprefix="€",
        separatethousands=True,
        range=[0, y_max]
    )

    return fig
