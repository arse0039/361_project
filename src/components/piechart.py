
import datetime
import plotly.graph_objects as go
from dash import Dash, html, dcc, Input, Output, State


def render(app: Dash) -> html.Div:
    @app.callback(
        Output('pie-graph', "figure"),
        Input('submit', 'n_clicks'),
        State('principal', 'value'),
        State('monthly', 'value'),
        State('interest', 'value'),
        State('years', 'value'))
    def comp_interest(n_clicks, principal, monthly, interest, time):
        yearly_principal = {}
        yearly_interest = {}
        interest = interest/100
        current_savings = principal
        interest_only = 0
        principal_only = current_savings
        for i in range(time):
            current_savings = current_savings * \
                pow((1 + (interest/12)), 12)
            interest_only += (current_savings - principal)
            principal_only += monthly*12
            current_savings += monthly*12
            principal = current_savings
            yearly_interest[datetime.date.today().year + (i+1)
                            ] = float('{0:.2f}'.format(interest_only))
            yearly_principal[datetime.date.today().year + (i+1)
                             ] = float('{0:.2f}'.format(principal_only))

        p = list(yearly_principal.values())
        i = list(yearly_interest.values())

        pie_vals = [i[-1], p[-1]]
        fig2 = go.Figure(
            go.Pie(labels=['Interest', 'Principal'], values=pie_vals))
        fig2.update_traces(hoverinfo='label+percent', textinfo='value')
        if n_clicks:
            return fig2

    return dcc.Graph(id="pie-graph", figure=go.Figure(go.Pie()))
