class Solution {
public:
    int hammingDistance(int x, int y) {
        // 这道题让我求两个数字之间的汉明距离，两个数字之间的汉明距离就是其二进制数对应位不同的个数，
        // 那么最直接了当的做法就是按位分别取出两个数对应位上的数并异或，我们知道异或的性质上相同的为0，不同的为1，我们只要
        // 把为1的情况累加起来就是汉明距离了. 我们可以一开始直接将两个数字异或起来，然后我们遍历异或结果的每一位，统计为1的个数
        
        int ans = 0;
        int temp = x ^ y;
        for (int i=0; i<32; i++){
            ans += (temp >> i) & 1;
        }
        return ans;
    }
};



