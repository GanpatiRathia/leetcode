class Solution:
    def isAnagram(self, s, t):
        """
        Given two strings s and t, return true if t is an anagram of s, and false otherwise.
        """
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for char in s:
            count_s[char] = count_s.get(char, 0) + 1

        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        return count_s == count_t
