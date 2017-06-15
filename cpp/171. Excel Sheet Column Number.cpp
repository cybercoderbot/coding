/*Related to question Excel Sheet Column Title
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
*/

/*二十六进制转十进制的问题，一位一位的转换即可*/

class Solution {
public:
    int titleToNumber(string s) {
        int ans = 0, w = 1;
        for (int i = s.size(); i>0; i--){
            ans += (s[i-1] - 'A' + 1) * w;
            w *= 26;
        }
        return ans;
    }
};



