import datetime
import plotly.graph_objects as go
from dash import Dash, html, dcc, Input, Output, State


def render(app: Dash) -> html.Div:
    @app.callback(
        # receive data from stored session and use data to
        # populate pie chart graph
        Output('pie-graph', 'figure'),
        Input('submit', 'n_clicks'),
        Input('data-storage', 'data'))
    def comp_interest(n_clicks, data):
        """ This is a callback function that generates the data
        needed to populate the pie chart. """
        principal = data[0]['principal']
        interest = data[0]['interest']
        monthly = data[0]['monthly']
        time = data[0]['years']

        yearly_principal = {}
        yearly_interest = {}
        interest = interest/100
        current_savings = principal
        interest_only = 0
        principal_only = current_savings

        # For loop to calculate data for each individual year,
        # which is stored in a dictionary with the year as the key
        # and the monetary value as the value.
        for i in range(time):
            # algorithm for calculating compounding interest per year
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

        # access only the monetary data for use in the pie chart
        principal_data = list(yearly_principal.values())
        interest_data = list(yearly_interest.values())

        # generate the pie chart from the data
        pie_vals = [interest_data[-1], principal_data[-1]]

        fig2 = go.Figure(
            go.Pie(labels=['Interest', 'Principal'], values=pie_vals))
        fig2.update_traces(hoverinfo='label+percent',
                           textinfo='value')

        # create on-click event to populate the graph
        if n_clicks:
            return fig2

    return dcc.Graph(id="pie-graph", figure=go.Figure(go.Pie()))
