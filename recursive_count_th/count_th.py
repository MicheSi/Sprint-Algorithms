'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # base caes - if word is less than 2 letters, cannot contain 'th'
    if len(word) < 2:
        return 0
    # if letters after first 2 indexes are 'th', increase count by 1
    elif word[:2] == 'th':
        return count_th(word[2:]) + 1
    else:
        return count_th(word[1:])
