
import datetime
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, State


def render(app: Dash) -> html.Div:
    @app.callback(
        Output('future-graph', "figure"),
        Input('submit', 'n_clicks'),
        State('principal', 'value'),
        State('monthly', 'value'),
        State('interest', 'value'),
        State('time', 'value'))
    def comp_interest(n_clicks, principal, monthly_cont, interest, time_frame):
        yearly_total = {}
        yearly_principal = {}
        yearly_interest = {}

        current_savings = principal
        interest_only = 0
        interest = interest/100
        principal_only = current_savings
        for i in range(time_frame):
            current_savings = current_savings * pow((1 + (interest/12)), 12)
            interest_only += (current_savings - principal)
            principal_only += monthly_cont*12
            current_savings += monthly_cont*12
            principal = current_savings
            yearly_total[datetime.date.today().year + (i+1)
                         ] = float('{0:.2f}'.format(current_savings))
            yearly_interest[datetime.date.today().year + (i+1)
                            ] = float('{0:.2f}'.format(interest_only))
            yearly_principal[datetime.date.today().year + (i+1)
                             ] = float('{0:.2f}'.format(principal_only))

        years = list(yearly_total.keys())
        p = list(yearly_principal.values())
        i = list(yearly_interest.values())
        fig1 = go.Figure()
        fig1.add_trace(go.Bar(
            x=years,
            y=p,
            name='Principal',
            hovertemplate="Total Principal: %{y}"))
        fig1.add_trace(go.Bar(
            x=years,
            y=i,
            name="Interest",
            hovertemplate="Total Interest: %{y}"))

        fig1.update_layout(
            barmode='stack',
            title={'text': "Retirement Growth Chart",
                    'xanchor': 'center',
                    'yanchor': 'top',
                    'x': 0.5
                   },
            xaxis_title="Year",
            yaxis_title="Value (USD)",
            xaxis_dtick=1
        )

        if n_clicks:
            return fig1

    return dcc.Graph(id='future-graph', figure=go.Figure())
