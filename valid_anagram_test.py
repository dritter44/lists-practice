from valid_anagram import is_valid_anagram

def main():
    print("is t an anagram of s: " + str(is_valid_anagram('anagram','nagaram')))
    print("is t an anagram of s: " + str(is_valid_anagram('rat','car')))
    print("is t an anagram of s: " + str(is_valid_anagram('','nagaram')))
    print("is t an anagram of s: " + str(is_valid_anagram('ab','abc')))

main()