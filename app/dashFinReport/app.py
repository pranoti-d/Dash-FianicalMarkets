# -*- coding: utf-8 -*-
from flask import Flask, render_template
import dash
import dash_core_components as dcc
import dash_html_components as html
from app.server import AppServer
from dash.dependencies import Input, Output
from app.dashFinReport.pages import (
    overview,
    pricePerformance,
    portfolioManagement,
    feesMins,
    distributions,
    newsReviews,
)
from app.dashFinReport.utils import make_dash_table
import pandas as pd
import pathlib


# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("./data").resolve()

#Data
df_avg_returns = pd.read_csv(DATA_PATH.joinpath("df_avg_returns.csv"))
df_after_tax = pd.read_csv(DATA_PATH.joinpath("df_after_tax.csv"))
df_recent_returns = pd.read_csv(DATA_PATH.joinpath("df_recent_returns.csv"))

server = AppServer

app = dash.Dash(__name__, server=server, title="Demo App", meta_tags=[{"name": "viewport", "content": "width=device-width"}])


#app = dash.Dash(
#    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
#)
#server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/dash-financial-report/sector-trends":
        return pricePerformance.create_layout(app)
    elif pathname == "/dash-financial-report/company-trends":
        return portfolioManagement.create_layout(app)
    elif pathname == "/dash-financial-report/valuation":
        return feesMins.create_layout(app)
    elif pathname == "/dash-financial-report/distributions":
        return distributions.create_layout(app)
    elif pathname == "/dash-financial-report/news-and-reviews":
        return newsReviews.create_layout(app)
    elif pathname == "/dash-financial-report/full-view":
        return (
            overview.create_layout(app),
            pricePerformance.create_layout(app),
            portfolioManagement.create_layout(app),
            feesMins.create_layout(app),
            distributions.create_layout(app),
            newsReviews.create_layout(app),
        )
    else:
        return overview.create_layout(app)


@app.callback(
dash.dependencies.Output('data', 'children'),
[dash.dependencies.Input('dropdown', 'value')])
def update_output(fig_name):
    return filterdata(fig_name)


def filterdata(fig_name):
    print(fig_name)
    lst = ['-']
    lst.append(fig_name)
    df_avg_returns_filter = df_avg_returns[df_avg_returns['A'].isin(lst)]
    df_avg_returns_data = df_avg_returns_filter.drop(['A'], axis =1)
    return html.Table( make_dash_table(df_avg_returns_data),
                       className="tiny-header",)

@app.callback(
dash.dependencies.Output('data1', 'children'),
[dash.dependencies.Input('dropdown', 'value')])
def update_output1(fig_name):
    return filterdata1(fig_name)   

def filterdata1(fig_name):
    print(fig_name)
    lst = ['-']
    lst.append(fig_name)
    df_after_tax_filter = df_after_tax[df_after_tax['A'].isin(lst)]
    df_after_tax_data = df_after_tax_filter.drop(['A'], axis =1)
    return html.Table( make_dash_table(df_after_tax_data),
                       className="tiny-header",)



@app.callback(
dash.dependencies.Output('data2', 'children'),
[dash.dependencies.Input('dropdown', 'value')])
def update_output2(fig_name):
    return filterdata2(fig_name)   

def filterdata2(fig_name):
    print(fig_name)
    lst = ['HD']
    lst.append(fig_name)
    df_recent_returns_filter = df_recent_returns[df_recent_returns['A'].isin(lst)]
    df_recent_returns_data = df_recent_returns_filter.drop(['A'], axis =1)
    return html.Table( make_dash_table(df_recent_returns_data),
                       className="tiny-header",)




