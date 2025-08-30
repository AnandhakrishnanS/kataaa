# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

def duplicate_count(text):
    text=text.lower()
    text_list=[x for x in text ]
    counter=0
    for i in text_list:
        if text_list.count(i)>1:
            prin
            counter+=1
            text_list=[x for x in text_list if x!=i ]
    return counter
