import re, nltk
from nltk.corpus import stopwords

with open("miracle_in_the_andes.txt", "r") as file:
    book = file.read()

pattern = re.compile(r"\w+")
findings = re.findall(pattern, book.lower())

d = {}

for word in findings:
    if word in d.keys():
        d[word] += 1
    else:
        d[word] = 1

dlist = [(word, count) for word, count in d.items()]
dlist = sorted(dlist, key = lambda x: x[1], reverse=True)

nltk.download('stopwords')
black_list = stopwords.words("english")

filtered_words = list(filter(lambda x: x[0] not in black_list, dlist))
print(filtered_words[:10])
