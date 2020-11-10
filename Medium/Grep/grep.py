import sys

def execute_grep(search, text):
    search_length = len(search)
    text_length = len(text)
    index_search = 0
    index_text = 0
    index_text_start = 0
    write_to_index_text_start = True
    while index_text < text_length:
        t = text[index_text]
        s = search[index_search]
        if text[index_text] == search[index_search]:
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
            return text

if __name__ == "__main__":
    execute_grep("llo", "helllo")
    # execute_grep(str(sys.argv[1]), str(sys.argv[2]))