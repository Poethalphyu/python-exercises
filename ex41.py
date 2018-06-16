import random
from urllib.request import urlopen
import sys
WORD_URL="http://learncodethehardway.org/words.txt"
WORDS=[]
PHRASES={"class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
        "class %%%(object):\n\tdef _init_(self,***)":
        "class %%% has-a  _init_that takes self and *** params.",
        "class %%%(object):\n\tdef  ***(self,@@@):
        "class %%% has-a function *** that takes self and @@@ params.",
        "*** = %%%()":
        "Set *** to an instance of class %%%.",
        "***.***(@@@)":
        "From *** get the *** function,call it with params self,@@@.",
        "***.***='***'":
        "From *** get the *** attribute and set it to '***'."}
if len(sys.argv) == 2 and sys.argv[1] == "english":
PHRASES_FIRST=True
else:
PHRASES_FIRST=False
for word in urlopen(WORLD_URL.readlines():
WORDS.appen(str(word.strip(),encoding="utf-8"))
def convert(snippet,phrase):
class_names=[w.capitalized() for w in
random.sample(WORDS,snippet.count("%%%"))]
other_names=random.sample(WORDS,sinppet.count("***"))
results=[]
param_name=[]
for i in range(0,snippet.count("@@@")):
param-count=random.randint(1,3)
param_names.append(','.join(
radom.sample(WORDS,param_count)))
for word in class_names:
result=result.replace("%%%",word,1)
for word in other_names:
result=result.replace("@@@",word,1)
results.append(result0
return results
try:
while True:
snippes=list(PHRASES.keys())
random.shuffle(snippets)
for snippet in snippets:
phrase=PHRASES[snippet,phrase)
if PHRASES_FIRST:
question,answer=answer,question
print(question)
input(">")
print(f"ANSWER: {answer}\n\")
except EOFError:
print("\nBye")
