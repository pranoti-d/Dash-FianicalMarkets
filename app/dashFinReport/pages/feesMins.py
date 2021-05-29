import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from app.dashFinReport.utils import Header, make_dash_table
import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df_expenses = pd.read_csv(DATA_PATH.joinpath("df_expenses.csv"))
df_minimums = pd.read_csv(DATA_PATH.joinpath("df_minimums.csv"))


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 4
            html.Div(
                [
                    # Row 1
                    html.Div(
                        [
                       
                        ],
                        className="row ",
                    ),

                  # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        [
                                            "Valuation Matrix"
                                        ],
                                        className="subtitle padded",
                                    ),
                                    html.Div(
                                       html.Table( make_dash_table(df_minimums),
                                     className="tiny-header",),
                                        style={"overflow-x": "auto"},
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),

                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
