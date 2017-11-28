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
    ListNode* reverseList(ListNode* head) {
        ListNode* new_head = new ListNode(0);
        new_head -> next = head;
        ListNode* prev = new_head;
        ListNode* curr = head; 
        while (curr && curr -> next) {
            ListNode* temp = prev -> next;
            prev -> next = curr -> next;
            curr -> next = curr -> next -> next; 
            prev -> next -> next = temp;
        }
        return new_head -> next;
    }
};




