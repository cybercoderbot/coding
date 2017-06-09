/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        // 建立一个新链表，然后把输入的两个链表从头往后撸，每两个相加，
        // 添加一个新节点到新链表后面，就是要处理下进位问题。
        // 还有就是最高位的进位问题要最后特殊处理一下.
        
        ListNode* res = new ListNode(-1);
        ListNode* curr = res;
        int carry = 0;
        while(l1 || l2){
            int n1 = l1? l1->val : 0;
            int n2 = l2? l2->val : 0;
            int sum = n1 + n2 + carry;
            carry = sum /10;
            curr->next = new ListNode(sum%10);
            curr = curr->next;
            l1 = l1? l1->next : NULL;
            l2 = l2? l2->next : NULL;
        }
        if(carry){
            curr->next = new ListNode(1);
        }
        return res->next;
    }
};



