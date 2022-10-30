from dash import Dash
from src.components import layout
import dash_bootstrap_components as dbc


def main():
    app = Dash(external_stylesheets=[{"rel": "stylesheet"}])
    app.title = "Retirement Calculator"
    app.layout = layout.render_layout(app)
    app.run()


if __name__ == "__main__":
    main()
