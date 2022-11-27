from dash import Dash, html, dcc
from . import retirement_forecaster, inputs, piechart, microservice


def render_layout(app: Dash):
    return html.Div(
        children=[
            html.Div(children=[
                html.H1(app.title),
                html.P(
                    "Curious if you are on track for healthy nest egg for retirement?"),
                html.P(
                    "Use this tool to help you plan how much you should invest in order to hit your financial goals at retirement."),
                html.P(
                    "Simply add the data below and click the button to populate your forecast graph. Update your values and click calculate to update the graphs."
                ),
                html.Hr(),
            ]),
            html.Div(children=[inputs.render(app)]),
            microservice.render(app),
            html.Div(className='graph-div',
                     children=[
                         html.Div(className='graph',
                                  id="bar-graph", children=[retirement_forecaster.render(app)]),
                         html.Div(className='graph', id="pie", children=[
                                  piechart.render(app)])
                     ]),
            dcc.Store(id='data-storage', data=[], storage_type='session')
        ]
    )
