class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Optimization 1: Early exit if magazine is shorter than ransomNote.
        # This is a quick check that avoids unnecessary counting.
        if len(ransomNote) > len(magazine):
            return False

        # Use a list of 26 integers for character counts (for lowercase English letters)
        # This is often faster than a dictionary for fixed-size alphabets
        # as it avoids hashing and dynamic resizing overhead.
        magazine_counts = [0] * 26 

        # Populate counts for magazine
        # ord(char) - ord('a') converts 'a' to 0, 'b' to 1, etc.
        for char_code in map(ord, magazine):
            magazine_counts[char_code - ord('a')] += 1

        # Check against ransomNote
        for char_code in map(ord, ransomNote):
            index = char_code - ord('a')
            if magazine_counts[index] > 0:
                magazine_counts[index] -= 1  # Use the character
            else:
                return False  # Not enough of this character
                
        return True