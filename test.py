
import datetime
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html

current_savings = 7500.00
monthly_cont = 300.00
time_frame = 15
intr = 10/100

yearly_total = {}
yearly_principal = {}
yearly_interest = {}
interest_only = 0
principal_only = current_savings
principal_total = current_savings + (((monthly_cont)*12)*time_frame)


def comp_interest(starting_value, monthly_cont, interest, time_frame):
    yearly_total = {}
    yearly_principal = {}
    yearly_interest = {}

    current_savings = starting_value
    interest_only = 0
    principal_only = current_savings
    for i in range(time_frame):
        current_savings = current_savings * pow((1 + (interest/12)), 12)
        interest_only += (current_savings - starting_value)
        principal_only += monthly_cont*12
        current_savings += monthly_cont*12
        starting_value = current_savings
        yearly_total[datetime.date.today().year + (i+1)
                     ] = float('{0:.2f}'.format(current_savings))
        yearly_interest[datetime.date.today().year + (i+1)
                        ] = float('{0:.2f}'.format(interest_only))
        yearly_principal[datetime.date.today().year + (i+1)
                         ] = float('{0:.2f}'.format(principal_only))
    return(yearly_total, yearly_principal, yearly_interest)


result = comp_interest(7500, 300, 0.1, 10)
years = list(result[0].keys())
p = list(result[1].values())
i = list(result[2].values())
fig1 = go.Figure(go.Bar(x=years, y=p, name='Principal')
                 )
fig1.add_trace(go.Bar(x=years, y=i, name="Interest"))

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

pie_vals = [i[-1], p[-1]]
fig2 = go.Figure(go.Pie(labels=['Interest', 'Principal'], values=pie_vals))
fig2.update_traces(hoverinfo='label+percent', textinfo='value')


app = dash.Dash()
app.layout = html.Div([
    html.Div(dcc.Graph(figure=fig1)),
    html.Div(dcc.Graph(figure=fig2))
])

app.run_server()
