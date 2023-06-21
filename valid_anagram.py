def is_valid_anagram(s,t):
    # its a valid anagram if the counts of each letter is the same
    # quick way, implement a dict as a hashset
    # sort each string, then use pointers to see if each iterator is equal
    s_sorted = sorted(s.lower())
    t_sorted = sorted(t.lower())
    n = len(s_sorted)
    o = len(t_sorted)
    if n != o:
        return False
    for letter in range(0,n):
        if s_sorted[letter] != t_sorted[letter]:
            return False

    return True

# really good answer: sort and join the strings, then see if equal
# def isAnagram(self, s: str, t: str) -> bool:
#         s_srtd = "".join(sorted(s))
#         t_srtd = ''.join(sorted(t))
#         if s_srtd == t_srtd:
#             return True
#         else:
#             return False