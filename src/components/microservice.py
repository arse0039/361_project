from dash import Dash, html, Input, Output, State


def render(app: Dash) -> html.Div:
    @app.callback(
        # Receive data from stored session and update txt file with said data.
        Output('monthly-target', "children"),
        Input('submit', 'n_clicks'),
        Input('data-storage', 'data'))
    def monthly_savings(n_clicks, data):
        import time

        principal = data[0]['principal']
        interest = data[0]['interest']
        years = data[0]['years']

        goal = 1000000

        with open('user_input.txt', 'w') as saving_data:
            saving_data.writelines(
                f'{interest/100}, {goal}, {principal}, {years}')

        time.sleep(1)

        with open('monthly_savings_amount.txt') as goal:
            final = goal.readlines()[0]

        with open('user_input.txt', 'w') as clear:
            pass

        if n_clicks:
            return f'In order to reach one million dollars, you would need to save ${final} per month for the next {years} years.'

    return html.Div(id="monthly-target")
