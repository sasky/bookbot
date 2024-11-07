
def main():
    generate_report("books/frankenstein.txt")


def generate_report(path_to_book):
    book = generate_string_from_txt_file(path_to_book)
    words = count_words(book)
    each_char_counted = count_each_char_in_string(book)
    each_char_sorted = sort_char_count_by_num(each_char_counted)
    
    print(f"--- Begin report of {path_to_book} ---")
    print(f"{words} words found in the document")
    print("")
    for char, num in each_char_sorted.items():
        print(f"The '{char}' character was found {num} times")
    print("--- End report ---")

def count_words(string:str)->int:
    return len(string.split())


def generate_string_from_txt_file(path_to_book:str)->str:
    with open(path_to_book) as f:
        return  f.read()
 
def count_each_char_in_string(str:str):
    dict = {}
    for c in str.lower():
        if c.isalpha():
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1
    return dict


def sort_char_count_by_num(dict = {}):
    # covert to name /values 
    name_values_list = []
    for char, num in dict.items():
        name_values_list.append({'char' : char, 'num' : num })


    # run the sort
    name_values_list.sort(reverse=True, key=sort_on)
    # convert back to the  dict structure we had originally
    result = {}
    for i in name_values_list:
        result[i['char']] = i['num']

    return result

def sort_on(dict= []):
    return dict["num"]


main()
