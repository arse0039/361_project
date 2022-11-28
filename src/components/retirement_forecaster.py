import datetime
import plotly.graph_objects as go
from dash import Dash, dcc, Input, Output


def render(app: Dash) -> dcc.Graph:
    @app.callback(
        # receive data from stored session and use data to
        # populate bar chart graph
        Output('future-graph', 'figure'),
        Input('submit', 'n_clicks'),
        Input('data-storage', 'data'))
    def comp_interest(n_clicks, data):
        principal = data[0]['principal']
        interest = data[0]['interest']
        monthly_cont = data[0]['monthly']
        time_frame = data[0]['years']

        yearly_total = {}
        yearly_principal = {}
        yearly_interest = {}

        current_savings = principal
        interest_only = 0
        interest = interest/100
        principal_only = current_savings

        # For loop to calculate data for each individual year,
        # which is stored in a dictionary with the year as the key
        # and the monetary value as the value.
        for i in range(time_frame):
            # algorithm for calculating compounding interest per year
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
        principal_data = list(yearly_principal.values())
        interest_data = list(yearly_interest.values())

        # create the table figure from the data
        fig1 = go.Figure()
        fig1.add_trace(go.Bar(
            x=years,
            y=principal_data,
            name='Principal',
            hovertemplate="Total Principal: %{y:$.2f}"))
        fig1.add_trace(go.Bar(
            x=years,
            y=interest_data,
            name="Interest",
            hovertemplate="Total Interest: %{y:$.2f}"))

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

        # create on-click event to populate the graph
        if n_clicks:
            return fig1

    return dcc.Graph(id='future-graph', figure=go.Figure())
