/*Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants 
represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between 
answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
 

Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
*/

/*这道题给了我们两个字符串数组，让我们找到坐标位置之和最小的相同的字符串。那么对于这种数组项和其坐标之间关系的题，
最先考虑到的就是要建立数据和其位置坐标之间的映射。我们建立list1的值和坐标的之间的映射，然后遍历list2，如果当前遍历到的
字符串在list1中也出现了，那么我们计算两个的坐标之和，如果跟我们维护的最小坐标和min_sum相同，那么将这个字符串加入结果ans中，
如果比min_sum小，那么min_sum更新为这个较小值，然后将结果ans清空并加入这个字符串*/


class Solution{
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2){
        vector<string> ans;
        unordered_map<string, int> m;
        int min_sum = INT_MAX, sum = 0;
        for (int i=0; i<list1.size(); i++){
            m[list1[i]] = i;
        }
        for (int i=0; i<list2.size(); i++){
            if (m.count(list2[i])){
                sum = i + m[list2[i]];
                if (sum == min_sum){
                    ans.push_back(list2[i]);
                }else if (sum < min_sum){
                    min_sum = sum;
                    ans = {list2[i]};
                }
            }
        }
        return ans;
    }
    
};
