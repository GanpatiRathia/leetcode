from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Step 1: Count character frequencies in the magazine
        magazine_counts = Counter(magazine)
        
        # Step 2: Count character frequencies in the ransomNote
        ransom_note_counts = Counter(ransomNote)
        
        # Step 3: Check if ransomNote can be constructed
        # For each character and its count in ransomNote_counts,
        # ensure that magazine_counts has at least that many occurrences.
        for char, count in ransom_note_counts.items():
            if magazine_counts[char] < count:
                return False  # Not enough characters in magazine
                
        return True # All characters can be constructed