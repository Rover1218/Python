text = "hello world"
replacements = {"hello": "hi", "world": "earth"}
result = ' '.join(replacements.get(word, word) for word in text.split())
print(result)