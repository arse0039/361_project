from dash import Dash, html
from . import retirement_forecaster, inputs, piechart


def render_layout(app: Dash):
    return html.Div(
        children=[
            html.Div(children=[
                html.H1(app.title),
                html.P(
                    "Curious if you are on track for healthy nest egg for retirement?"),
                html.P(
                    "Use this tool to help you plan how much you should invest in order to hit your financial goals at retirement."),
                html.Hr(),
            ]),
            html.Div(children=[inputs.render(app)]),
            html.Div(children=[retirement_forecaster.render(
                app), piechart.render(app)]),

        ]
    )
