Given a string s, find the length of the longest substring without duplicate characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

# Solution

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        ans = 0
        # charToNextIndex stores the index after current character
        charToNextIndex = {}
        print("charToNextIndex initial", charToNextIndex)
        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in charToNextIndex:
                print("charToNextIndex", charToNextIndex)
                print("s[j]", s[j])
                i = max(charToNextIndex[s[j]], i)

            ans = max(ans, j - i + 1)
            charToNextIndex[s[j]] = j + 1

        return ans