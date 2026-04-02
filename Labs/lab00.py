# Lab00, CS 9, Romina Sarfehnia
# Romina Sarfehnia

def found_in_list(list1, list2):
    ''' When analyzing potentially malicious network traffic, analysts often
    need to check if suspicious IP addresses or domains appear in known
    threat intelligence lists.
    This function takes two lists as its parameters (list1 and
    list2). Return True if each element in list1 exists in list2.
        Return False otherwise. If list1 contains no elements, return True.

    '''
    compare_list = []
    for num1 in list1:
        for num2 in list2:
            if num1 == num2:
                compare_list.append(num1)
        
    return compare_list == list1
                

assert found_in_list(["one",2], [0,"one",2,"three"]) == True
assert found_in_list([], [1,2,3,4]) == True
assert found_in_list(["192.68.35.33","128.66.3.48"], ["128.67.3.148"]) == False
assert found_in_list([1,2,3], [3,2,1]) == True

def alternate_case(text):
    ''' In cybersecurity, obfuscation techniques are common. Malware authors
    often use case alternation to evade simple string matching in security
    tools. Security analysts need to normalize text for proper analysis.

    This function takes a string parameter (text) and returns a new
        string that flips the case of each alpha character in the provided text.

    '''
    swapped_string = ""
    for i in range(len(text)):
        swapped_string = swapped_string + text[i].swapcase()

    return swapped_string

assert alternate_case("") == ""
assert alternate_case("This is a Sentence") == "tHIS IS A sENTENCE"
assert alternate_case("CS9") == "cs9"
assert alternate_case("9.95") == "9.95"

def get_counts(text):
    ''' Character frequency analysis is crucial in cryptography and for detecting
    encoding anomalies in suspicious files or communications.

    This function takes a string parameter (text) and returns a dictionary
        type where each key in the dictionary is a unique upper-case character
        in `text` and its associated value is the number of occurrences of the
        unique character in text. Note that the unique characters should be case
        insensitive ("a" and "A" are considered the same and should be stored as
        "A" in the dictionary). Non-alpha characters (including whitespaces)
        and their occurrences should also be stored in the dictionary.
    '''
    new_dict = {}
    for letter in text:
        letter = letter.upper()
        if letter in new_dict:
            new_dict[letter] += 1
        else:
            new_dict[letter] = 1

    return new_dict

dict1 = get_counts("This is a Sentence")
assert dict1.get("S") == 3
assert dict1.get("P") == None
assert dict1.get("I") == 2
assert dict1.get(" ") == 3

dict2 = get_counts("Pi is Approximately 3.14159")
assert dict2.get("1") == 2
assert dict2.get("A") == 2
assert dict2.get("P") == 3
assert dict2.get(".") == 1
assert dict2.get(4) == None

def swap_key_val(database):
    """ In security operations, data often needs to be reorganized for different
    types of lookups or to create reverse mappings.

        The function expects a database to be a dictionary.
        Assuming that an input dictionary has unique values for each key,
        return a new dictionary with the keys and values swapped.
    """
    new_dict = {}
    values = list(database.values())
    keys = list(database.keys())
    for i in range(len(database)):
        new_dict[values[i]] = keys[i]

    return new_dict

weaknesses = {"CWE-20": "Improper Input Validation", "CWE-287": "Improper Authentication" }
reverse_weaknesses = swap_key_val(weaknesses)
assert reverse_weaknesses["Improper Authentication"] == "CWE-287"
