/*3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.
*/

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        set<char> t;
        int len=0, left=0, right=0;
        while (right < s.size()){
            // s[right] not in set
            if (t.find(s[right]) == t.end()){
                t.insert(s[right++]);
                len = max(len, (int) t.size());
            }else{
                // s[right] in set
                t.erase(s[left++]);
            }
        }
        return len;
    }
};