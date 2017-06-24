/*Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".*/

/*用了两个指针i,j分别指向a和b的末尾，然后每次取出一个字符，转为数字，若无法取出字符则按0处理，然后定义进位carry，初始化为0，
将三者加起来，对2取余即为当前位的数字，对2取商即为当前进位的值，记得最后还要判断下carry，如果为1的话，要在结果最前面加上一个1*/

class Solution {
public:
    string addBinary(string a, string b) {
        string ans = "";
        int i = a.size()-1, j = b.size()-1, carry=0;
        while (m>=0 || n>=0){
            int x = m>=0? a[i--] - '0' : 0;
            int y = n>=0? b[j--] - '0' : 0;
            int sum = x + y + carry;
            ans = to_string(sum%2) + ans;
            carry = sum / 2;
        }
        return carry==1? "1" + ans : ans;
    }
};




