import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from app.dashFinReport.utils import Header, make_dash_table
import pandas as pd
import pathlib


# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


df_current_prices = pd.read_csv(DATA_PATH.joinpath("df_current_prices.csv"))
df_hist_prices = pd.read_csv(DATA_PATH.joinpath("df_hist_prices.csv"))
df_avg_returns = pd.read_csv(DATA_PATH.joinpath("df_avg_returns.csv"))
df_after_tax = pd.read_csv(DATA_PATH.joinpath("df_after_tax.csv"))
df_recent_returns = pd.read_csv(DATA_PATH.joinpath("df_recent_returns.csv"))
df_graph = pd.read_csv(DATA_PATH.joinpath("df_graph.csv"))

sector_names = ['Auto', 'Retail']


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 2
            html.Div(
                [

                   # Row
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.P(["Select Sector"], style={"color": "#7a7a7a", "font-size": "20px","margin-bottom": "30px"}),
                                ],
                                className="four columns",
                            ),
                             html.Div([
                                dcc.Dropdown(
                                    id='dropdown',
                                    options=[{'label': x, 'value': x} for x in sector_names],
                                    value='Auto'
                                )], 
                             className="six columns",    
                            ),
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
                                            "Profit & Loss Statement"
                                        ],
                                        className="subtitle padded",
                                    ),
                                    html.Div(
                                        id='data',
                                        style={"overflow-x": "auto"},
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        [
                                            "Balance Sheet"
                                        ],
                                        className="subtitle padded",
                                    ),
                                    html.Div(
                                        id='data1',
                                        style={"overflow-x": "auto"},
                                    ),
                                ],
                                className=" twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 5
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Recent investment returns"],
                                        className="subtitle padded",
                                    ),
                                    html.Table(
                                        id='data2',
                                        className="tiny-header",
                                    ),
                                ],
                                className=" twelve columns",
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


