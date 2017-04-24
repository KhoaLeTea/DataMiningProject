"""
# start w/ >100 reviews (7845), drop to >30 w/ good processing flow (27387)
"""
import json
# import plotly
# import plotly.graph_objs as go

infile = 'JSON/yelp_academic_dataset_business.json'
outfile = 'JSON/businesses_many_reviews.json'
offset, count = 0, 0
# review_count = []
over_hundred = 0
write_str = ""


def delete_contents(file_name):
    with open(file_name, "w") as f:
        pass

delete_contents(outfile)
with open(infile) as i_f, open(outfile, "a") as o_f:
    
    businessList = []
    
    if offset:
        i_f.seek(offset, 0)  # seek from the beginning of the file to offset

    for line in i_f:
        obj = json.loads(line)
        # review_count.append(obj['review_count'])
        reviews = obj['review_count']
        if reviews > 100:
            business_id = obj['business_id']
            name = obj['name']
            city = obj['city']
            state = obj['state']
            latitude = float(obj['latitude'])
            longitude = float(obj['longitude'])
            stars = obj['stars']
            businessList.append({})
            json.dump({'business_id': business_id, 'name': name,
                       'city': city, 'state': state, 'latitude': latitude,
                       'longitude': longitude, 'stars': stars,
                       'review_count': reviews}, o_f)
            o_f.write("\n")
            # o_f.write(write_str)
            over_hundred += 1
        if over_hundred > 2:
            break
        count += 1

print over_hundred


with open(outfile) as f:
    for line in f:
        data = json.loads(line)
        print data['business_id']
# trace0 = go.Histogram(x=review_count)
# data = [trace0]
# layout = go.Layout(
#     title='Review Count by Business',
#     xaxis=dict(
#         title='Review Count',
#         titlefont=dict(size=18)
#     ),
#     yaxis=dict(
#         title='Number of Businesses',
#         titlefont=dict(size=18)
#     )
# )
#
# fig = go.Figure(data=data, layout=layout)
# plotly.offline.plot(fig, filename='review_count_histogram.html')
print "Done!"
