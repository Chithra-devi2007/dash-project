import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# 1. Dash App-ai thodanguval
app = Dash(__name__)

# 2. Data-vai load seithal (Unga file name: formatted_output.csv)
df = pd.read_csv("formatted_output.csv")

# Date column-ai date format-ku matri, chronological order-la varisai paduthudhal
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values(by="Date")

# 3. Line Chart uruvakkudhal
fig = px.line(
    df,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={"Date": "Date of Sale", "Sales": "Total Revenue ($)"},
)

# Chart style - Pink Morsel pink color!
fig.update_traces(line_color="#ec4899", line_width=2)
fig.update_layout(
    title_font_size=20,
    hovermode="x unified",
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
)

# Price hike date (Jan 15, 2021) kaata oru vertical reference line
fig.add_vline(
    x="2021-01-15",
    line_width=2,
    line_dash="dash",
    line_color="#374151",
    annotation_text="Price Increase (Jan 15, 2021)",
    annotation_position="top left",
)

# 4. Web page layout வடிவமைப்பு
app.layout = html.Div(
    style={
        "fontFamily": "Segoe UI, sans-serif",
        "backgroundColor": "#f9fafb",
        "padding": "40px",
    },
    children=[
        # Title (Header)
        html.Header(
            style={
                "textAlign": "center",
                "marginBottom": "30px",
                "borderBottom": "2px solid #e5e7eb",
                "paddingBottom": "20px",
            },
            children=[
                html.H1(
                    "Soul Foods Pink Morsel Sales Visualizer",
                    style={"color": "#1f2937", "margin": "0 0 10px 0"},
                ),
                html.P(
                    "Analyzing sales before and after the January 15, 2021 price increase.",
                    style={"color": "#4b5563", "margin": "0", "fontSize": "16px"},
                ),
            ],
        ),
        # Graph Component
        html.Div(
            style={
                "backgroundColor": "#ffffff",
                "borderRadius": "8px",
                "boxShadow": "0 4px 6px -1px rgba(0, 0, 0, 0.1)",
                "padding": "20px",
            },
            children=[
                dcc.Graph(id="sales-line-chart", figure=fig),
            ],
        ),
    ],
)

# 5. Server-ai iyakkudhal
if __name__ == "__main__":
    app.run_server(debug=True)
