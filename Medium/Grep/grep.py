import sys


def execute_grep(search, lines):
    if len(search) < 1:
        return "Please provide at least 1 character."
    dict = {}
    result = {}
    counter = 0
    for line in lines:
        dict[counter] = line
        counter = counter + 1
    for index, line in dict.items():
        if check_line(search, line):
            result[index] = line
    return result


def check_line(search, line):
    search_length = len(search)
    line_length = len(line)
    index_search = 0
    index_text = 0
    index_text_start = 0
    write_to_index_text_start = True
    while index_text < line_length:
        if line[index_text] == search[index_search]:
            if write_to_index_text_start:
                index_text_start = index_text + 1
                write_to_index_text_start = False
            index_search = index_search + 1
            index_text = index_text + 1
        elif index_search != 0:
            index_search = 0
            index_text = index_text_start
            write_to_index_text_start = True
        else:
            index_search = 0
            index_text = index_text + 1
        if search_length == index_search:
            return True
    return False


if __name__ == "__main__":
    execute_grep("llo", ["hello", "helllo", "world", "llllllllo", "llooo", "helo"])
    # execute_grep(str(sys.argv[1]), str(sys.argv[2]))
