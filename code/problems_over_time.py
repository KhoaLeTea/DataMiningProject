"""
download docs: CLA
python
import nltk
nltk.download()
select appropriate packages on GUI and download


*******http://firstmonday.org/ojs/index.php/fm/article/view/4944/3863#p2
"""

# strip fillers, then can graph (scatter) VADER sentiment about business over time
# stem, then analyze common collocations involving the words "issue", "problem", etc.

# need to normalize issue dist. by # of reviews received for particular period - week; month?

import json
from time import clock
import os
import nltk
from string import punctuation
import plotly
import plotly.graph_objs as go
from nltk import FreqDist
from nltk.corpus import wordnet as wn
import datetime


# negative_sentiment = ["worst", "rude", "terrible", "horrible", "bad", "awful",
#                       "disgusting", "bland", "tasteless", "gross", "mediocre",
#                       "overpriced", "worse", "poor", "flavorless",
#                       "disappoint"]  # added flavorless, disappoint
# first_person_plural = ["we", "us", "our", "ourselves"]  # removed "ours"
# third_person = ["she", "he", "her", "him"]
# past_tense_verbs = ["was", "were", "asked", "told", "said", "did", "charged",
#                     "waited", "left", "took"]
# narrative_sequencers = ["after", "then"]
# common_nouns = ["manager", "waitress", "waiter", "customer", "attitude",
#                 "waste", "poisoning", "money", "bill", "minutes"]
#                 # removed "customers"; redundant from stemming
#
# low_rating_words = [negative_sentiment, first_person_plural, third_person,
#                     past_tense_verbs, narrative_sequencers, common_nouns]
# low_rating = negative_sentiment + first_person_plural + third_person  \
#              + past_tense_verbs + narrative_sequencers + common_nouns



# categories: 1. service issue; 2. food issue; 3. price issue; 4. undetermined
service_issue = ["rude",
                 "asked", "told", "said", "did", "waited", "took",
                 "after", "then",
                 "manager", "waitress", "waiter", "attitude", "bill", "minutes"]
food_issue = ["disgusting", "bland", "tasteless", "gross", "flavorless",
              "poisoning"]
price_issue = ["overpriced", "charged", "waste", "money", "bill"]
undet_issue = ["worst", "terrible", "horrible", "bad", "awful", "mediocre",
               "worse", "poor", "disappoint",
               "we", "us", "our", "ourselves",
               "she", "he", "her", "him",
               "was", "were", "left",
               "customer"]
issue_list = [service_issue, food_issue, price_issue, undet_issue]

dates, rounded_dates = [], []
service_list, food_list, price_list, undet_list = [], [], [], []
month_buckets, counts = [], []


def main():

    stopword_list = str_tuple(nltk.corpus.stopwords.words('english'))
    porter = nltk.PorterStemmer()
    service_stems = [porter.stem(w).encode('utf-8') for w in service_issue]
    food_stems = [porter.stem(w).encode('utf-8') for w in food_issue]
    price_stems = [porter.stem(w).encode('utf-8') for w in price_issue]
    undet_stems = [porter.stem(w).encode('utf-8') for w in undet_issue]

    path = 'JSON/over_1000_reviews/'
    count = 0
    with open(path + str(os.listdir(path)[1])) as infile:

        for line in infile:
            service, food, price, undet = 0, 0, 0, 0
            obj = json.loads(line)
            d = datetime.datetime.strptime(obj['date'], "%Y-%m-%d")

            round_d = d.replace(day=1)
            if round_d not in month_buckets:
                month_buckets.append(round_d)
                counts.append(1)
            else:
                counts[month_buckets.index(round_d)] += 1

            if obj['stars'] <= 3:  # additional processing
                count += 1

                text = str_tuple(obj['text'].split())
                tokens = [w.lower().strip(punctuation) for w in text
                          if w not in stopword_list]
                stems = [porter.stem(t.decode('utf-8')) for t in tokens]
                stems = [s.encode('utf-8') for s in stems]  # ???

                for s in service_stems:
                    if s in stems:
                        service += 1
                for f in food_stems:
                    if f in stems:
                        food += 1
                for p in price_stems:
                    if p in stems:
                        price += 1
                for u in undet_stems:
                    if u in stems:
                        undet += 1

                total_issue_stems = service + food + price + undet
                if total_issue_stems >= 5:  # threshold exceeded, calculate percentages
                    dates.append(d)

                    service_per = service / float(total_issue_stems)
                    food_per = food / float(total_issue_stems)
                    price_per = price / float(total_issue_stems)
                    undet_per = undet / float(total_issue_stems)

                    service_list.append(service_per)
                    food_list.append(food_per)
                    price_list.append(price_per)
                    undet_list.append(undet_per)
                    # print "service: " + str(service_per)
                    # print "food: " + str(food_per)
                    # print "price: " + str(price_per)
                    # print "undet: " + str(undet_per)
                    # print "\n"

            # if count > 10:
            #     break


def str_tuple(t, encoding="utf-8"):
    return tuple([i.encode(encoding) for i in t])

main()


d_sort, s_sort, f_sort, p_sort, u_sort = zip(*sorted(zip(dates, service_list, food_list, price_list, undet_list)))
rd_sort = sorted(rounded_dates)

print "Processing finished; making scatterplot..."
trace0 = go.Scatter(x=d_sort, y=s_sort, name='Service Issue')  # mode='markers'
trace1 = go.Scatter(x=d_sort, y=f_sort, name='Food Issue')  # mode='markers'
trace2 = go.Scatter(x=d_sort, y=p_sort, name='Price Issue')  # mode='markers'
trace3 = go.Scatter(x=d_sort, y=u_sort, name='Unresolved Issue')  # mode='markers'
trace4 = go.Scatter(x=rd_sort, y=s_sort, name='Service Issue Rounded')

data = [trace0, trace1, trace2, trace3]
layout = go.Layout(
    title='Issue Distribution Over Time',
    xaxis=dict(
        title='Date',
        titlefont=dict(size=18)
    ),
    yaxis=dict(
        title='Issue Percentage',
        titlefont=dict(size=18)
    )
)
fig = go.Figure(data=data, layout=layout)
# plotly.offline.plot(fig, filename='issue_distribution.html')

trace5 = go.Scatter(x=month_buckets, y=counts, name='Review Count', mode='markers')
data = [trace5]
layout = go.Layout(
    title='Count of Reviews by Month',
    xaxis=dict(
        title='Month',
        titlefont=dict(size=18)
    ),
    yaxis=dict(
        title='Count',
        titlefont=dict(size=18)
    )
)
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='month_buckets.html')

print "Done!"
