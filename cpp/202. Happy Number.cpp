/*Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by 
the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops 
endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
*/

/*对于某一个正整数，如果对其各个位上的数字分别平方，然后再加起来得到一个新的数字，再进行同样的操作，如果最终结果变成了1，则说明是快乐数，
如果一直循环但不是1的话，就不是快乐数，那么现在任意给我们一个正整数，让我们判断这个数是不是快乐数，题目中给的例子19是快乐数，那么我们来看
一个不是快乐数的情况，比如数字11有如下的计算过程：

1^2 + 1^2 = 2
2^2 = 4
4^2 = 16
1^2 + 6^2 = 37
3^2 + 7^2 = 58
5^2 + 8^2 = 89
8^2 + 9^2 = 145
1^2 + 4^2 + 5^2 = 42
4^2 + 2^2 = 20
2^2 + 0^2 = 4

算到最后时数字4又出现了，那么之后的数字又都会重复之前的顺序，这个循环中不包含1，那么数字11不是一个快乐数。我们可以用set来记录所有
出现过的数字，然后每出现一个新数字，在set中查找看是否存在，若不存在则加入表中，若存在则跳出循环，并且判断此数是否为1，若为1返回true，
不为1返回false*/

class Solution {
public:
    bool isHappy(int n) {
        set<int> s;
        while (n!=1){
            int x = 0;
            while (n){
                x += (n % 10) * (n % 10);
                n /= 10;
            }
            n = x;
            if (s.count(n)) break;
            else s.insert(n);
        }
        return n == 1;   
    }
};



