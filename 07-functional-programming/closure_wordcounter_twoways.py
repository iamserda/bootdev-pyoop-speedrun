def word_count_aggregator():
    """Returns a function that can count the number of words within a given sentence."""
    count = 0
    def word_finder(doc):
        """A recursive closure(func + its lexical scope) that finds and keeps count of words in a string."""
        nonlocal count
        if not doc:
            count += 0
        else:
            items = doc.split(" ", maxsplit=1)
            items_len = len(items)
            if items_len >= 1:
                count += 1 # new word found
                if items_len == 2:
                    # we may have more words, we should continue search for words.
                    word_finder(items[1])
        return count
    return word_finder

def word_count_aggregator1():
    count = 0
    def word_finder(doc):
        nonlocal count
        count += len(doc.split(" "))
        return count
    return word_finder

sentence = 'A closure is a function that references variables from outside its own function body.'
assert word_count_aggregator()(sentence) == 14
assert word_count_aggregator1()(sentence) == 14