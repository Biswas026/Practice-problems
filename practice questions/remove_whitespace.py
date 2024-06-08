import re
sentence = "I am a sentence with lot of white spaces"
sentence_no_whitespace = re.sub(r"\s+", "", sentence, flags=re.UNICODE)

print(sentence_no_whitespace)
