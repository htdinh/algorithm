"""
Constraints:

s.length == 5
'A' <= s[0] <= s[3] <= 'Z'
'1' <= s[1] <= s[4] <= '9'
s consists of uppercase English letters, digits and ':'.
"""

import string
from typing import List

ALL_CHARS = string.ascii_uppercase
CHAR_MAP = {char: idx for idx, char in enumerate(ALL_CHARS)}


class Solution(object):

    def cellsInRange1(self, s:str) -> List:
        """
        :type s: str
        :rtype: List[str]
        """
        """
        Time O(size output), space O(1)
        """
        ans = []
        start_char, start_idx, _, end_char, end_idx = list(s)
        for char in ALL_CHARS[CHAR_MAP[start_char]:CHAR_MAP[end_char] + 1]:
            for idx in range(int(start_idx), int(end_idx) + 1):
                ans.append(char + str(idx))
        return ans

    def cellsInRange2(self, s:str) -> List:
        """
        Improvement: Not using the global mapping, instead use `chr` and `ord` to convert between string and Unicode code point
        """
        ans = []
        for c in range(ord(s[0]), ord(s[3])+1):
            for i in range(int(s[1]), int(s[4])+1):
                ans.append(chr(c) + str(i))
        return ans

    def cellsInRange3(self, s:str) -> List:
        """
        Improvement: Exploit the order of the unicode code point, no need to convert '1' -> 1
        """
        c1, r1, _, c2, r2 = map(ord, s)
        return [chr(c) + chr(r) for c in range(c1, c2 + 1) for r in range(r1, r2 + 1)]

