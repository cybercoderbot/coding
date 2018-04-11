/*
170. Two Sum III - Data structure design
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,

add(1); add(3); add(5);
find(4) -> true
find(7) -> false 
*/


#include <unordered_map>

class TwoSum {
private:
    std::unordered_map<int,int> _m;
    
public:
    /** Initialize your data structure here. */
    TwoSum() {
    }
    
    /** Add the number to an internal data structure.. */
    void add(int number) {
        _m[number]++;
    }
    
    /** Find if there exists any pair of numbers which sum is equal to the value. */
    bool find(int value) {
        for (auto n: _m){
            int d = value - n.first;
            //如果当前值不等于差值d，那么只要哈希表中有差值d就返回True，或者是
            //当差值d等于当前值时，如果此时哈希表的映射次数大于1，则表示哈希表中还有
            //另一个和当前值相等的数字，二者相加就是目标值
            if ((d != n.first && _m.count(d)) || (d==n.first && n.second >1)){
                return true;
            }
        }
        return false;
        
    }
};

/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum obj = new TwoSum();
 * obj.add(number);
 * bool param_2 = obj.find(value);
 */