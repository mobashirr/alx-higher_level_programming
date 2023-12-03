#!/usr/bin/python3

def multiple_returns(sentence):

    if len(sentence) == 0 or not sentence:
        return (0, None)

    c = sentence[0]
    return (len(sentence), c)


'''
# test case:
sentence = "At school, I learnt C!"
length, first = multiple_returns("")
print("Length: {:d} - First character: {}".format(length, first))
'''
