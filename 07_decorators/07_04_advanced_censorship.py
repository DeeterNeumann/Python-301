# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crap")` would censor the words "shoot" and "crap".

import re

def selective_censorship(*censored_words):
    def censor(initial_func):
        def wrapper(*args, **kwargs):
            # offensive_words = ["shoot", "fuck", "shit", "damn"]
            censored = initial_func(*args, **kwargs)
            for word in censored_words:
                offensive_word = r'\b' + re.escape(word) + r'\b'
                censored = re.sub(offensive_word, lambda match: match.group(0)[0] + "*" * (len(match.group(0))-1), censored)
            print(censored)
            return censored
        return wrapper
    return censor

@selective_censorship("shoot", "crap")            
def offensive(something):
    return something

offensive("oh shoot! this is some crap!")



# import re

# def censor(initial_func):
#     def wrapper(*args, **kwargs):
#         offensive_words = ["shoot", "crap"]
#         censored = initial_func(*args, **kwargs)
#         for word in offensive_words:
#             offensive_word = r'\b' + re.escape(word) + r'\b'
#             censored = re.sub(offensive_word, lambda match: match.group(0)[0] + "*" * (len(match.group(0))-1), censored)
#         print(censored)
#         return censored
#     return wrapper

# @censor            
# def offensive(something):
#     return something
