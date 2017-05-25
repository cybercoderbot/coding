class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        
        // 这道题要我们从有序数组中去除重复项，和Remove Duplicates from Sorted List(移除有序链表中的重复项) 
        // 的题很类似，但是要简单一些，因为数组的值可以通过下标直接访问，而链表不行。那么这道题的解题思路是，
        // 我们使用快慢指针来记录遍历的坐标，最开始时两个指针都指向第一个数字，
        // 如果两个指针指的数字相同，则快指针向前走一步，如果不同，则两个指针都向前走一步，
        // 这样当快指针走完整个数组后，慢指针当前的坐标加1就是数组中不同数组的个数
        
        int n = nums.size();
        if (n <= 1) return n;
        int pre = 0, cur = 0;
        while (cur < n) {
            if (nums[cur] == nums[pre]) ++cur;
            else nums[++pre] = nums[cur++];
        }
        return pre + 1;
    }
};




