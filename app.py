import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, dcc, html

# 1. Dash App-ai thodanguval
app = Dash(__name__)

# 2. Data-vai load seithal
df = pd.read_csv("formatted_output.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values(by="Date")

# 3. Web page layout வடிவமைப்பு (With CSS Styling)
app.layout = html.Div(
    style={
        "fontFamily": "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
        "backgroundColor": "#f0f2f5",
        "padding": "40px 20px",
        "minHeight": "100vh",
    },
    children=[
        # Title (Header Card)
        html.Header(
            style={
                "textAlign": "center",
                "marginBottom": "40px",
                "backgroundColor": "#ffffff",
                "padding": "30px",
                "borderRadius": "12px",
                "boxShadow": "0 4px 15px rgba(0, 0, 0, 0.05)",
            },
            children=[
                html.H1(
                    "Soul Foods Pink Morsel Sales Visualizer",
                    style={
                        "color": "#1e293b",
                        "margin": "0 0 10px 0",
                        "fontSize": "32px",
                        "fontWeight": "700",
                    },
                ),
                html.P(
                    "Interactive sales analysis dashboard before and after the January 15, 2021 price increase.",
                    style={"color": "#64748b", "margin": "0", "fontSize": "16px"},
                ),
            ],
        ),
        # Control Panel (Radio Buttons Side/Top Card)
        html.Div(
            style={
                "backgroundColor": "#ffffff",
                "borderRadius": "12px",
                "boxShadow": "0 4px 15px rgba(0, 0, 0, 0.05)",
                "padding": "25px",
                "marginBottom": "30px",
                "textAlign": "center",
            },
            children=[
                html.Label(
                    "Select Region:",
                    style={
                        "fontWeight": "600",
                        "color": "#334155",
                        "marginRight": "20px",
                        "fontSize": "18px",
                    },
                ),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": " All Regions", "value": "all"},
                        {"label": " North", "value": "north"},
                        {"label": " East", "value": "east"},
                        {"label": " South", "value": "south"},
                        {"label": " West", "value": "west"},
                    ],
                    value="all",  # Default valua 'all' irukum
                    inline=True,
                    style={"display": "inline-block"},
                    inputStyle={"marginRight": "5px", "marginLeft": "20px"},
                    labelStyle={
                        "color": "#475569",
                        "fontSize": "16px",
                        "cursor": "pointer",
                    },
                ),
            ],
        ),
        # Graph Component Card
        html.Div(
            style={
                "backgroundColor": "#ffffff",
                "borderRadius": "12px",
                "boxShadow": "0 4px 15px rgba(0, 0, 0, 0.05)",
                "padding": "20px",
            },
            children=[
                dcc.Graph(id="sales-line-chart"),
            ],
        ),
    ],
)


# 4. Callback to filter data based on Radio Button selection
@app.callback(Output("sales-line-chart", "figure"), Input("region-filter", "value"))
def update_graph(selected_region):
    # Filter condition
    if selected_region == "all":
        filtered_df = df
        title_text = "Pink Morsel Sales Over Time - All Regions"
    else:
        filtered_df = df[df["region"].str.lower() == selected_region.lower()]
        title_text = f"Pink Morsel Sales Over Time - {selected_region.capitalize()} Region"

    # Create figure
    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        title=title_text,
        labels={"Date": "Date of Sale", "Sales": "Total Revenue ($)"},
    )

    # Apply modern styles to the line and chart
    fig.update_traces(line_color="#db2777", line_width=2.5)  # Vibrant Pink
    fig.update_layout(
        title_font_size=20,
        title_font_color="#1e293b",
        hovermode="x unified",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=True, gridcolor="#e2e8f0"),
        yaxis=dict(showgrid=True, gridcolor="#e2e8f0"),
    )

    # Price hike reference line
    fig.add_vline(
        x="2021-01-15",
        line_width=2,
        line_dash="dash",
        line_color="#64748b",
        annotation_text="Price Increase (Jan 15, 2021)",
        annotation_position="top left",
        annotation_font_color="#475569",
    )

    return fig


# 5. Server-ai iyakkudhal
if __name__ == "__main__":
    app.run_server(debug=True)
