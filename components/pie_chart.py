import plotly.express as px

def pie_chart(df):

    pie_chart = px.pie(
        df, 
        values='Amount', 
        names='Category', 
        color='Category',
        hole=0.5,
        color_discrete_map={
            'Total Net Savings':'#1F3A8A',
            'Total Projected Portfolio':'#60A5FA'}
             )

    pie_chart.update_layout(
        margin=dict(l=0, r=0, t=0, b=50),  # add top margin for legend
        legend=dict(
            orientation="h",      # horizontal legend
            yanchor="top",
            y=1.3,
            xanchor="center",
            x=0.5 ,                 # center horizontally
            xref="paper",
            yref="paper",
        ),
        paper_bgcolor='rgba(0,0,0,0)'
    )

    pie_chart.update_traces(
        textinfo='percent',
        textfont_size=12,
        hovertemplate='<b>%{label}</b><br>Amount: %{value:,.0f}<br>Share: %{percent}<extra></extra>',
        marker=dict(line=dict(color='white', width=3)),
    )

    return pie_chart