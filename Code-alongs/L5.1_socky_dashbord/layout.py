from dash import html, dcc
import dash_bootstrap_components as dbc


class Layout:
    def __init__(self, symbol_dict: dict) -> None:

        self._symbol_dict = symbol_dict

        self._stock_options_dropdown = [
            {"label": name, "value": symbol} for symbol, name in symbol_dict.items()
        ]

        self._ohlc_options = [
            {"label": option, "value": option}
            for option in ("open", "high", "low", "close")
        ]

        self._slider_marks = {
            i: mark
            for i, mark in enumerate(
                ["1 day", "1 week", "1 months", "3 months", "1 year", "5 year", "Max"]
            )
        }

    def layout(self):

        return dbc.Container(
            [
                dbc.Card(
                    dbc.CardBody(html.H1("Techy stocks viewer")), class_name="mt-3"
                ),
                dbc.Row(
                    class_name="mt-4",
                    children=[
                        dbc.Col(
                            html.P("Choose a stock"),
                            class_name="mt-1",
                            lg="4",
                            xl={"offset": 2, "size": 2},
                        ),
                        dbc.Col(
                            dcc.Dropdown(
                                id="stockpicker-dropdown",
                                options=self._stock_options_dropdown,
                                value="AAPL",
                            ),
                            xs=12,
                            sm=12,
                            md=6,
                            lg="4",
                            xl="3",
                        ),
                        dbc.Col(
                            dbc.Card(
                                dcc.RadioItems(
                                    id="ohlc-radio",
                                    options=self._ohlc_options,
                                    className="m-1",
                                    value="close",
                                )
                            ),
                            xs=12,
                            sm=12,
                            md=6,
                            lg="4",
                            xl=3,
                        ),
                    ],
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Graph(id="stock-graph"),
                                dcc.Slider(
                                    id="time-slider",
                                    min=0,
                                    max=6,
                                    marks=self._slider_marks,
                                    value=2,
                                    step=None,
                                ),
                            ],
                            xs=12,
                            sm=12,
                            md=3,
                            lg={"size": "6"},
                            xl=6,
                        ),
                        dbc.Col(
                            [
                                dbc.Row(
                                    dbc.Card(
                                        [
                                            html.H2(
                                                "Highest value",
                                                className="h5 mt-3 mx-3",
                                            ),
                                            html.P(
                                                id="highest-value",
                                                className="h1 mx-2 text-success",
                                            ),
                                        ]
                                    ),
                                    class_name="mt-5 h-25",
                                ),
                                dbc.Row(
                                    dbc.Card(
                                        [
                                            html.H2(
                                                "Lowest value",
                                                className="h5 mt-3 mx-3",
                                            ),
                                            html.P(
                                                id="lowest-value",
                                                className="h1 mx-2 text-danger",
                                            ),
                                        ]
                                    ),
                                    class_name="mt-5 h-25",
                                ),
                            ],
                            xs=12,
                            sm=12,
                            md=3,
                            xl=6,
                        ),
                    ]
                ),
                # storing intermediate value on clients browser in order to share between several callbacks
                dcc.Store(id="filtered-df"),
            ]
        )
