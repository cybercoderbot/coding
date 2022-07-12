/*Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit 
signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your 
function returns 0 when the reversed integer overflows.
*/


class Solution {
public:
    int reverse(int x) {
        if(x==0) return 0;
        int sign = x>0? 1: -1;
        x = abs(x);
        long long res = 0;
        while (x > 0) {
            res = res * 10 + x % 10;
            x /= 10;
        }
        if (res > INT_MAX) return 0;
        return sign * res;
    }
};

