# obtain a list of files in the input directory

from ._internals.count_words import count_words
from ._internals.preprocess_lines import preprocess_lines
from ._internals.read_all_lines import read_all_lines
from ._internals.split_in_words import split_in_words
from ._internals.write_count_words import write_count_words


def main():
    
    all_lines = read_all_lines()

    ## preprocess_lines
    all_lines = preprocess_lines(all_lines)

    ## split_in_words
    words = split_in_words(all_lines)

    ## count_words
    counter = count_words(words)

    # count the frequency of the words in the files in the input directory
    # counter={}
    # for filename in input_file_list:
    #     with open('data/input/'+filename) as f:
    #         for l in f:
    #             for w in l.split( ):
    #                 w = w.lower().strip(",.!?")
    #                 counter[w] = counter.get(w, 0) + 1


    write_count_words(counter)

if __name__ == "__main__":
     main()