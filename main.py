# @author - Aditya Chaudhary
# Sentiment analysis from scratch
# Algorithm used will be
# 1. Cleaning the text
#  a.Create a text file and read the text from it
#  b.lower the text because "aditya" is not equal to "Aditya"
#  c.Remove the Punctuations
# 2. Remove Stopwords(words which are not)
# 3. Now ur list of words from the string should be compared with our emotions list


# Let's Go... !
import string
from collections import Counter
import matplotlib.pyplot as plt
text = open("sample.txt", encoding="utf-8").read()

# Conversion to lowercase
lower_text = text.lower()
# print("Converting to lowercase :" + " " + lower_text)

# Remove the punctuation  ['!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~']
clean_text = lower_text.translate(str.maketrans('', '', string.punctuation))
# print("After pronounciation removal :" + " " + clean_text)

# Conversion of string to list
clean_text = clean_text.split()

# Removal of stopwords(Words which doesn't make sense !)
stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
             "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
             "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
             "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
             "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
             "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
             "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
             "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
             "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
             "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_text = []

for word in clean_text:
    if word not in stopwords:
        final_text.append(word)

# Open Emotion file and compare our clean_text list to emotion file
emotion_list = []
with open("emotions.txt", 'r') as file:
    for line in file:
        finished_text = line.replace(
            "\n", "").replace("'", "").replace(",", "").strip()
        word, emotion = finished_text.split(":")
        if word in final_text:
            emotion_list.append(emotion)

# Count each emotions
emotion_count = Counter(emotion_list)
print(emotion_count)


# plot the graph

fig, ax1 = plt.subplots()
ax1.bar(emotion_count.keys(), emotion_count.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
