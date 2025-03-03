# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normall return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"

import re

def censor(initial_func):
    def wrapper(*args, **kwargs):
        offensive_words = ["shoot", "crap"]
        censored = initial_func(*args, **kwargs)
        for word in offensive_words:
            offensive_word = r'\b' + re.escape(word) + r'\b'
            censored = re.sub(offensive_word, lambda match: match.group(0)[0] + "*" * (len(match.group(0))-1), censored)
        print(censored)
        return censored
    return wrapper

@censor            
def offensive(something):
    return something


offensive("Oh shoot!")
offensive("Oh crap!")