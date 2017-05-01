"""

"""


import json
from time import clock
import bisect

businesses = 'JSON/businesses_many_reviews.json'
reviews = 'JSON/yelp_academic_dataset_review.json'
offset_b, offset_r = 0, 0
business_list = []

t1 = clock()
b_count, r_count = 0, 0


def index(a, x, yes, no):
    # Locate the leftmost value exactly equal to x
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        yes += 1
    else:
        no += 1
    return yes, no

with open(businesses) as b:

    if offset_b:
        b.seek(offset_b, 0)  # seek from beginning of the file to offset

    for line in b:
        obj = json.loads(line)
        business = obj['business_id']
        bisect.insort(business_list, str(business))
        b_count += 1
        # if b_count >= 5:
        #     break
    t2 = clock()
    print "Done putting businesses in a list, time elapsed: " + str(t2 - t1)

with open(reviews) as r:

    if offset_r:
        r.seek(offset_r, 0)

    yes, no = 0, 0
    for line in r:
        try:
            offset_r += len(line)
            obj = json.loads(line)
            business = obj['business_id']
            old_yes = yes
            yes, no = index(business_list, business, yes, no)
            if old_yes + 1 == yes:  # write review to file keyed w/ business_id
                business_file = 'JSON/over_1000_reviews/' + str(obj['business_id']) + '.json'
                with open(business_file, "a") as f:
                    f.write(line)

            r_count += 1
            if r_count % 100000 == 0:
                print "processed " + str(r_count) + " of 4153150 ("  \
                      + str(round((r_count/float(4153150))*100, 4)) + "%)"

        except KeyboardInterrupt:
            # can use offset_r to start processing at point in file where
            # processing was terminated with f.seek(offset) in another run
            print "\n" + str(offset_r)
            break
    print "yes, no: " + str(yes) + ", " + str(no)


t3 = clock()
print "Done matching business ids, total time elapsed: " + str(t3 - t1)

print r_count, b_count
