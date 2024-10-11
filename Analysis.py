import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Load the dataset
df = pd.read_csv('sales_data_sample.csv')

# Convert ORDERDATE to datetime
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Sales Data Analysis Dashboard"),

    # Dropdown for selecting product line
    dcc.Dropdown(
        id='product-line-dropdown',
        options=[{'label': line, 'value': line} for line in df['PRODUCTLINE'].unique()],
        value=df['PRODUCTLINE'].unique()[0],
        clearable=False
    ),

    # Bar chart for total sales by product line
    dcc.Graph(id='sales-by-product-line'),

    # Line chart for sales over time
    dcc.Graph(id='sales-over-time'),

    # Pie chart for order status distribution
    dcc.Graph(id='order-status-distribution')
])

@app.callback(
    Output('sales-by-product-line', 'figure'),
    Output('sales-over-time', 'figure'),
    Output('order-status-distribution', 'figure'),
    Input('product-line-dropdown', 'value')
)
def update_graphs(selected_product_line):
    filtered_df = df[df['PRODUCTLINE'] == selected_product_line]

    # Bar chart
    sales_by_product_line = filtered_df.groupby('PRODUCTLINE')['SALES'].sum().reset_index()
    bar_fig = px.bar(sales_by_product_line, x='PRODUCTLINE', y='SALES', title='Total Sales by Product Line')

    # Line chart
    sales_over_time = filtered_df.groupby('ORDERDATE')['SALES'].sum().reset_index()
    line_fig = px.line(sales_over_time, x='ORDERDATE', y='SALES', title='Sales Over Time')

    # Pie chart
    order_status_counts = filtered_df['STATUS'].value_counts().reset_index()
    order_status_counts.columns = ['Status', 'Count']
    pie_fig = px.pie(order_status_counts, values='Count', names='Status', title='Order Status Distribution')

    return bar_fig, line_fig, pie_fig

if __name__ == '__main__':
    app.run_server(mode='inline')
