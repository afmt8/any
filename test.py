import re
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


words_positive = [
    "grateful", "amazing", "wonderful", "beautiful", "sweet", "perfect",
    "kind", "generous", "help", "loved", "intelligent", "talented",
    "young", "bright", "passionate", "determined", "good", "friends", "fun"
]


words_negative = [
    "anxious", "stressed", "worst", "grumpy", "drained", "awful",
    "overslept", "missed", "uneasy", "boss", "noise", "dreadful", "lonely"
]

def classify_sentences(text):

    sentences = text.split('\n')
    #print(sentences)
    classified_sentences = {"positive": [], "negative": []}
    for sentence in sentences:
        positive_count = sum(word.lower() in words_positive for word in sentence.split())
        negative_count = sum(word.lower() in words_negative for word in sentence.split())
        
        
        if positive_count > negative_count:
            classified_sentences["positive"].append(sentence)
        elif negative_count > positive_count:
            classified_sentences["negative"].append(sentence)

    return classified_sentences


file= read_file("tweets.txt")
print("###############################################################")
#print(file )
##classify_sentences(file)
classified_sentences = classify_sentences(file)

print("Positive sentences:")
for sentence in classified_sentences["positive"]:
    print(sentence)


print("\nNegative sentences:")
for sentence in classified_sentences["negative"]:
    print(sentence)