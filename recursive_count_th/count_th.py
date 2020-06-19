'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, counter = None):
    #two counters
    #one starts at zero, and one starts at one
    if len(word) > 0:
        first = 0
        second = 1
    if len(word) == 0:
        return 0

    #need the counter to be used repeatedly in recursion
    if counter is None:
        counter = 0

    #base case - if second counter reaches end of the array 
    if first == len(word) - 1:
        return counter

    #if they add up to 'th', increment count
    if word[first] + word[second] == 'th':
        counter += 1

    #recurse on incremented counter
    first += 1
    second += 1

    return count_th(word[first:], counter) 



word = 'the sun beats down on the thick forest'

print(count_th(word))
