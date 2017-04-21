"""
Create 2d histogram (x=sentiment, y=star rating, z=count) of
'<sentiment>,<star rating>' output of 'extract_sentiment_and_stars.py' using
plotly (https://plot.ly/python/). Figures in code/visualizations as
'sentiment_star_histogram_top_excluded.png', 'sentiment_star_histogram_all'.

Requires: plotly
"""

import plotly
import plotly.graph_objs as go

infile = "JSON/sentiment_stars_tenpercent_sample.txt"

count = 0
sentiment, star = [], []

print "Initialized; processing data file..."
with open(infile) as f:
    for line in f:
        sentiment_val = float(line[0:-3])
        if sentiment_val < 0.8:
            sentiment.append(sentiment_val)
            star.append(int(line[-2:-1]))
        count += 1


print "Processing finished; making histogram..."
trace0 = go.Histogram2d(x=sentiment, y=star)
data = [trace0]
layout = go.Layout(
    title='Star Rating vs Sentiment',
    xaxis=dict(
        title='Sentiment',
        titlefont=dict(size=18)
    ),
    yaxis=dict(
        title='Star Rating',
        titlefont=dict(size=18)
    )
)

fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='sentiment_stars_2d_histogram_below_point8.html')
print "Done!"
