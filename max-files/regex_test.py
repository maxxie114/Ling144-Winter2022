# A program that filter out all of the urls in a paragraph
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
url_list = re.findall(regex, message)
# This will print everything that the regex captured
print(url_list)
# list of issues
issues = ["need help with programming", "need to look up python documentation",
          "need help with python issue", "need to ask question about python"]
# range(4) will generate a list of numbers between 0 and 4
for i in range(4):
    print(f"{issues[i]}: {url_list[i][0]}")