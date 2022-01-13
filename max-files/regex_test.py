import re

# A paragraph that contains some website
message = ("If you need help with programming, please look up your answer "
           "on https://www.google.com/, "
           "If you need to look up information on every single built-in "
           "function in python, please visit "
           "https://docs.python.org/3.8/library/index.html/, if you want to "
           "look up an answer of every single "
           "issue in the world in python, please visit "
           "https://stackoverflow.com/questions/tagged/python, finally "
           "if you want to ask question about anything you want in python, "
           "please ask them in the LING144 discord server: "
           "https://discord.gg/s7mHnCFhNN")

# A regular expression I made that can filter out most of the urls in ending in com,org,net,gg
regex = r"((https|http):\/\/[a-zA-Z0-9.]+?[a-zA-Z0-9]+\.(com|org|net|gg)[a-zA-Z0-9./]+\/?)"
# regex for finding the purpose of a url
find_context = r"(if[\w\s-]+(need|want)[\w\s-]+)"
url_list = re.findall(regex, message)
context_list = re.findall(find_context, message, re.IGNORECASE)

# nlp stuff
filtered_context_sentences = []
# a list that store all of sentences
context_sentences = []
stopwords = ["if","you","with","every","the","single","world","on","to","in","an","of","about","them","want","need","look","up"]
for sentence in context_list:
    lowered_sentence = sentence[0].lower()
    context_sentences.append(lowered_sentence)
    temp = lowered_sentence.split(" ")
    # filter out stopwords
    filtered_context_list = [words for words in temp if words not in stopwords]
    # insert a "need" at the front of the sentence
    filtered_context_list.insert(0, "need")
    filtered_context_sentences.append(" ".join(filtered_context_list))

# use len() just in case if there are more than 4 urls
for i in range(len(url_list)):
    print(f"{filtered_context_sentences[i]}: {url_list[i][0]}")