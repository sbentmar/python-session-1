import plotly.graph_objects as go

OUTPUT_FILE="my_figure.html"

fig = go.Figure(data = go.Scatter(
        x=[1,2,3,4,5,6,8],
        y=[1,2,3,4,5,6,7]
    )
)
fig.write_html(OUTPUT_FILE)
print("Wrote file to " + OUTPUT_FILE)