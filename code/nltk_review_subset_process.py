"""
Use VADER sentiment analysis tools (www.nltk.org/_modules/nltk/sentiment/vader.html)
to determine sentiment of reviews in yelp_academic_dataset_review.json. Will
also work with .csv files or to determine the sentiment of other pieces of
text, just change text_start and text_end accordingly.

Requires: NLTK; separate installation of VADER package.

'offset' is useful in case processing an entire file takes too long: change
'offset' from zero to the last printed value of 'offset' from the previous
processing run, then processing will start at that point in 'infile.'
"""

from time import clock

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

infile = "JSON/yelp_academic_dataset_review.json"

t1 = clock()
count = 0
neg_count, pos_count = 0, 0
avg_neg, avg_pos, avg_all = 0, 0, 0

offset = 0
text_start = 149
text_end = -48

with open(infile) as f:

    if offset:
        f.seek(offset, 0)  # seek from the beginning of the file to offset

    for line in f:
        if count > 10000:
            break
        count += 1
        offset += len(line)

        ss = sid.polarity_scores(line[text_start:text_end])

        # ignore reviews with 0.2 >= sentiment >= -0.2
        # TODO cutoff is somewhat arbitrary. find better cutoff?
        if ss['compound'] < -0.2:
            neg_count += 1
            avg_neg += ss['neg']
        elif ss['compound'] > 0.2:
            pos_count += 1
            avg_pos += ss['pos']

        if (count % 5000) == 0:
            print "Processing " + str(count) + " of 4153150 (%5.3f%%)" % ((count/float(4153150)) * 100)
            print "Offset: " + str(offset) + "\n"
        if (count % 100000) == 0:
            print "running totals:"
            print "neg_count" + str(neg_count)
            print "pos_count" + str(pos_count)
            print "avg_neg" + str(avg_neg/float(neg_count))
            print "avg_pos", (avg_pos/float(pos_count))
            print "avg_all", avg_all / float(count)
            print " "
        avg_all = avg_all + ss['pos'] - ss['neg']

print "Negative count: " + str(neg_count)
if neg_count > 0:
    print "Average neg score among negative reviews: " + str(avg_neg / float(neg_count)) + "\n"
else:
    print "No negative scores to average\n"

print "Positive count: " + str(pos_count)
if pos_count > 0:
    print "Average pos score among positive reviews: " + str(avg_pos / float(pos_count)) + "\n"
else:
    print "No positive scores to average\n"

print "Total average: " + str(avg_all / float(count))

t2 = clock()
print "Time elapsed: " + str(t2 - t1)
