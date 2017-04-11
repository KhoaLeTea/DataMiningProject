from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

infile = "JSON/reviews/yelp_academic_dataset_review.json"
# infile = "JSON/reviews/example.json"

count = 0
neg_count, pos_count = 0, 0
avg_neg, avg_pos = 0, 0
avg_all = 0

with open(infile) as f:
    for line in f:
        if count >= 100000:
            break
        count += 1
        ss = sid.polarity_scores(line[149:-48])

        # for k in sorted(ss):
        #     print k, ss[k],
        # print

        if ss['compound'] < -0.2:
            neg_count += 1
            avg_neg += ss['neg']
        elif ss['compound'] > 0.2:
            pos_count += 1
            avg_pos += ss['pos']
        if (count % 5000) == 0:
            print "Processing", count, "of 4153150 (%5.3f %%)" % ((count/float(4153150)) * 100)
        avg_all = avg_all + ss['pos'] - ss['neg']

print
print "Negative count: ", neg_count
print "Average neg score among negative reviews: ", avg_neg / float(neg_count)
print

print "Positive count: ", pos_count
print "Average pos score among positive reviews: ", avg_pos / float(pos_count)

print "Total average: ", avg_all / float(count)