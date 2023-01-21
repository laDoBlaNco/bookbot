# return list of words
def split_to_words(s):
    return s.split()
   
# return a dict of letter counts and a sorted list of alpha only keys    
def count_letters(s):
    letter_counts = {}
    letters = [letter.lower() for letter in s]
    for letter in letters:
        if letter in letter_counts:
            letter_counts[letter]+=1
        else:
            letter_counts[letter]=1
    
    sorted_items = list(letter_counts.items())
    sorted_items.sort(key=lambda a:a[1],reverse=True)         
    keys = [item[0] for item in sorted_items if item[0].isalpha()]
    return letter_counts,keys

def main():
    path = 'books/frankenstein.txt'
    with open(path) as f:
        file_contents = f.read() 

    words = split_to_words(file_contents)
    # print(len(words))

    # print(count_letters(file_contents))
    # print()
    
    counts,keys = count_letters(file_contents) 
    
    print(f"--- Begin report of {path} ---") 
    print(f"{len(words)} words found in the document\n\n")
    
    for l in keys:
        print(f"The '{l}' character was found {counts[l]} times") 
    
    print("--- End report ---") 

#-------------------------------
main() 
