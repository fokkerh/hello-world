# vervang woorden in string door ***
def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)
    return result

censored = censor('dit is een klote voorbeeld', 'klote')
print(censored)