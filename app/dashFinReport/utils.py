import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Img(
                        src=app.get_asset_url("logoblue.svg"),
                        className="logo",
                    ),
                    html.A(
                        html.Button("Print Report", id="learn-more-button"),
                        href="http://127.0.0.1:5000/printReport",
                    ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("IndiaDataHub Universe at a Glance")],
                        className="seven columns main-title",
                    ),
                    html.Div(
                        [
                            dcc.Link(
                                "Full View",
                                href="/dash-financial-report/full-view",
                                className="full-view-link",
                            )
                        ],
                        className="five columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "IndiaDataHub Universe",
                href="/dash-financial-report/overview",
                className="tab first",
            ),
            dcc.Link(
                "Sectoral Trends",
                href="/dash-financial-report/sector-trends",
                className="tab",
            ),
            dcc.Link(
                "Company Details",
                href="/dash-financial-report/company-trends",
                className="tab",
            ),
            dcc.Link(
                "Valuation Matrix", href="/dash-financial-report/valuation", className="tab"
            ),
            #dcc.Link(
            #    "Distributions",
            #    href="/dash-financial-report/distributions",
            #    className="tab",
            #),
            #dcc.Link(
            #    "News & Reviews",
            #    href="/dash-financial-report/news-and-reviews",
            #    className="tab",
            #),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
