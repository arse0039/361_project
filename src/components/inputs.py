from dash import Dash, Input, Output, State, dcc, html
import pandas as pd


def render(app: Dash) -> html.Div:
    @app.callback(
        Output('data-storage', 'data'),
        Input('submit', 'n_clicks'),
        State('principal', 'value'),
        State('monthly', 'value'),
        State('interest', 'value'),
        State('years', 'value')
    )
    def save_data(click, principal, monthly, interest, years):
        if click:
            data = [
                {'principal': principal,
                 'monthly': monthly,
                 'interest': interest,
                 'years': years
                 }]
            df = pd.DataFrame(data)
            return df.to_dict('records')

    return html.Div(
        children=[
            html.Div(children=[
                html.Div(children=[
                    html.Div(className="tooltip",
                             children=[' ? ', html.Span(
                                 className='tiptext', children=['Starting Balance is the amount of money you are currently starting with in your investment account.'])]
                             ),
                    html.Div(className="input-title",
                             children=["Starting Balance"]),
                    dcc.Input(type='number', id="principal", className="input",
                              placeholder='Enter starting balance', min=0),
                ]
                ),
                html.Div(children=[
                    html.Div(className="tooltip",
                             children=['?', html.Span(
                                 className='tiptext', children=['Annual interest is the average percentage of growth you expect each year on your investments.'])]
                             ),
                    html.Div(className="input-title",
                             children=["Annual Interest Rate"]),
                    dcc.Input(type='number', className='input', id='interest',
                              placeholder="Enter annual interest rate", min=1, max=20)
                ]
                ),
                html.Div(children=[
                    html.Div(className="tooltip",
                             children=['?', html.Span(
                                 className='tiptext', children=['Years until retirement is the number of years from the current year until the year you plan to retire.'])]
                             ),
                    html.Div(className="input-title",
                             children=["Years until retirement"]),
                    dcc.Input(type='number', id="years", className="input",
                                   placeholder='Enter years until retirement', min=0, max=50)
                ]
                ),
                html.Div(children=[
                    html.Div(className="tooltip",
                             children=['?', html.Span(
                                 className='tiptext', children=['Monthly Contributions is the average amount you plan to invest each month until retirement.'])]
                             ),
                    html.Div(className="input-title",
                             children=["Monthly Contributions"]),
                    dcc.Input(type='number', id="monthly", className='input',
                                   placeholder='Enter monthly contributions', min=0)
                ]
                ),
            ], className='inputs-div'),
            html.Button("Calculate", id='submit', n_clicks=0),
            html.Hr()
        ])
