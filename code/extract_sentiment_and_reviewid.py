"""
Extract and analyze infile for sentiment, then write to 'outfile' in format
'<sentiment>,<review_id>'.

Requires: NLTK; separate installation of VADER package.
"""

# sentiment analysis results, review ID

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

infile = 'JSON/yelp_tenpercent_sample.json'
outfile = 'JSON/sentiment_reviewid_tenpercent_sample.json'
infile_len = 414814
# infile_len = 4153150
count = 0


def delete_contents(file_name):
    with open(file_name, "w") as f:
        pass

# delete all contents of outfile
delete_contents(outfile)

with open(infile) as i_f, open(outfile, "a") as o_f:

    for line in i_f:
        count += 1

        ss = sid.polarity_scores(line[149:-48])
        compound_ss_score = ss['compound']
        review_id = line[14:36]

        write_str = str(compound_ss_score) + "," + str(review_id) + "\n"
        o_f.write(write_str)

        if count % 5000 == 0:
            print "Processing " + str(count) + " of " + str(infile_len) \
                  + " (%5.3f%%)" % ((count/float(infile_len)) * 100)
        # if count > 5:
        #     break
