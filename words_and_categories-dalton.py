words = ["worst", "rude", "terrible", "horrible", "bad", "awful", "disgusting",
         "bland", "tasteless", "gross", "mediocre", "overpriced", "worse",
         "poor", "flavorless", "disappoint", "we", "us", "our", "ourselves",
         "she", "he", "her", "him", "was", "were", "asked", "told", "said",
         "did", "charged", "waited", "left", "took", "after", "then", "manager",
         "waitress", "waiter", "customer", "attitude", "waste", "poisoning",
         "money", "bill", "minutes"]

# categories:
service = ["rude", "she", "he", "her", "him", "asked", "told", "said", "did", "waited", "left", "took", "after", "manager", "waitress", "waiter", "customer", "attitude", "minutes"]
food = ["disgusting", "bland", "tasteless", "gross", "flavorless", "poisoning"]
price = ["overpriced", "charged", "money", "bill", "waste"]
unresolved = ["worst", "terrible", "horrible", "bad", "awful", "mediocre", "worse", "poor", "disappoint", "we", "us", "our", "ourselves", "was", "were", "then"]  # catchall for words that don't fit in other categories
