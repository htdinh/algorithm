"""
Constraints:

1 <= pattern.length <= 20
1 <= words.length <= 50
words[i].length == pattern.length
pattern and words[i] are lowercase English letters.
"""

import string
from typing import List

ALPHABET = string.ascii_lowercase


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        """
        Approach: 'aqq' and 'aff' are to be mapped to same as 'qaa' or 'bcc'. Can we define a function to map them all
        to a unique value, then compare them? The mapping function is n-to-1.

        The what is important at the unique value is the distinct characters and the position of them. Exact char
        doesn't matter.
        """

        def convert_pattern(pattern):
            char_map = dict()  # Max size of this map is the number of unique characters in the alphabet
            i = 0
            ans = []
            for char in pattern:
                if char not in char_map:
                    char_map[char] = i
                    i += 1
                ans.append(ALPHABET[char_map[char]])
            # Time O(n) with n is the length of the pattern, space is also O(n) because each char must occupy one pos.
            # before joining into one variable
            return "".join(ans)

        key = convert_pattern(pattern)
        return [word for word in words if convert_pattern(word) == key]  # Compare two string => O(1) but in sequence
        # of O(n) in convert_pattern.

    def findAndReplacePattern2(self, words, p):
        """
        Improvement: this could extend when the number of unique characters in the pattern exceed 26, the size of
        all lowercase characters. The dictionary above would not have enough space to store that.
        """
        def F(w):
            m = {}
            return [m.setdefault(c, len(m)) for c in w]

        key = F(p)
        return [w for w in words if F(w) == key]  # Compare two list O(n) time and O(n) space, but in sequence of O(
        # n) in the F().