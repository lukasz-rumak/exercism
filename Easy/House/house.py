import sys


def recite_the_nursery_rhyme():
    beginning = ["This is", "that"]
    verb = ["belonged", "kept", "woke", "married", "kissed", "milked", "tossed", "worried", "killed", "ate", "lay in"]
    rest = ["the horse and the hound and the horn", "to the farmer sowing his corn",
            "the rooster that crowed in the morn", "the priest all shaven and shorn", "the man all tattered and torn",
            "the maiden all forlorn", "the cow with the crumpled horn", "the dog", "the cat", "the rat", "the malt",
            "the house that Jack built."]

    result = [[beginning[0] + " " + rest[len(rest) - 1]]]
    for i in range(1, len(rest)):
        tmp_array = [beginning[0] + " " + rest[len(rest) - i - 1]]
        tmp_counter = i
        for _ in range(i):
            tmp_array.append(beginning[1] + " " + verb[len(verb) - tmp_counter] + " " + rest[len(rest) - tmp_counter])
            tmp_counter = tmp_counter - 1
        result.append(tmp_array)
    return result


if __name__ == "__main__":
    recite_the_nursery_rhyme()
    #recite_the_nursery_rhyme(str(sys.argv[1]))