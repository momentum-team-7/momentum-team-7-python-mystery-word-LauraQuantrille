# 1. open word file and save as a variable - jupyter 9 X
# with open(file) as open_file: 
        # print(open_file.read())
        #print(type(read_file))
# 2. remove punctuation - jupypter 7 X
# 3. normalize all words to lowercase X
# 4. remove stop words - words used so frequently they are ignored X
# check each word and see if it's equal to one of the stop words or if it's in the list of stop words
# use conditional with if
# 5. go through file word by word and keep a count of how often each word is used


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    # open file and save as variable
    with open(file) as open_file:
        text = open_file.read()
        # make all text lowercase
        text = text.lower()
        words_count_list = {}
        # get rid of all punctuation
        text = text.replace("."," ")
        text = text.replace(","," ")
        text = text.replace("'"," ")
        text = text.replace(":"," ")
        text = text.replace("-"," ")
        text = text.replace("\n"," ")
        #turn text file into list
        text_list = text.split(" ")
        text_list_copy = text_list.copy()
        print(len(text_list_copy))
        
        for word in text_list:
            if word in STOP_WORDS:
                text_list_copy.remove(word)
            elif word not in words_count_list:
                temp_count = text_list_copy.count(word)
                words_count_list[word] = temp_count
        print(words_count_list)

        sorted_values = sorted(words_count_list.values(), reverse = True)
        sorted_dictionary = {}
        print(sorted_values)

        # sorted_dictionary
              
    
    



if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
