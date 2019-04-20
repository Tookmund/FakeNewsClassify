import nltk

import readFNC as ds

# Who are the authors we are analyzing?
authors = ("fake", "reliable")

author_tokens = {}
for a in authors:
    author_tokens[a] = []

TEST = int(ds.total/2)
for i in range(TEST):
    d = ds.data[i]
    author_tokens[d[1]].extend(d[0])

author_tokens["Disputed"] = []
correct_author = []
for i in range(TEST, ds.total):
    author_tokens["Disputed"].append(ds.data[i][0])
    correct_author.append(ds.data[i][1])

author_length_distributions = {}
correct = 0
# Calculate chisquared for each of the two candidate authors
for i in range(len(author_tokens["Disputed"])):
    d = author_tokens["Disputed"][i]
    da = {}
    for author in authors:
        # First, build a joint corpus and identify the 10 most frequent words in it
        joint_corpus = (author_tokens[author] + d)
        joint_freq_dist = nltk.FreqDist(joint_corpus)
        most_common = list(joint_freq_dist.most_common(10))

        # What proportion of the joint corpus is made up
        # of the candidate author's tokens?
        author_share = (len(author_tokens[author])
                        / len(joint_corpus))

        # Now, let's look at the 10 most common words in the candidate
        # author's corpus and compare the number of times they can be observed
        # to what would be expected if the author's papers
        # and the Disputed papers were both random samples from the same distribution.
        chisquared = 0
        for word,joint_count in most_common:

            # How often do we really see this common word?
            author_count = author_tokens[author].count(word)
            disputed_count = d.count(word)

            # How often should we see it?
            expected_author_count = joint_count * author_share
            expected_disputed_count = joint_count * (1-author_share)

            # Add the word's contribution to the chi-squared statistic
            chisquared += ((author_count-expected_author_count) *
                           (author_count-expected_author_count) /
                           expected_author_count)

            chisquared += ((disputed_count-expected_disputed_count) *
                           (disputed_count-expected_disputed_count)
                           / expected_disputed_count)
        da[author] = chisquared
    auth = min((v, k) for (k,v) in da.items())[1]
    if auth == correct_author[i]:
        correct += 1

print(correct/len(author_tokens["Disputed"]))
