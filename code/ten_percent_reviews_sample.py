from time import clock
import random

infile = "JSON/yelp_academic_dataset_review.json"
outfile = "JSON/yelp_tenpercent_sample.json"

count = 0
t1 = clock()

# no arg initializes to current time or "an OS-specific randomness source"
random.seed()
save_index = random.randint(0, 9)


def delete_contents(file_name):
    with open(file_name, "w") as f:
        pass

# delete all contents of outfile
delete_contents(outfile)

with open(infile) as i_f, open(outfile, "a") as o_f:
    for line in i_f:
        count += 1
        save_decision = random.randint(0, 9)
        if save_decision == save_index:
            o_f.write(line)

t2 = clock()
print "Time elapsed for " + str(count) + " lines: " + str(t2 - t1) + "seconds"