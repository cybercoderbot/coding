/*Iterative solution: 在原链表之前建立一个dummy node，因为首节点会变，然后从head开始，
将之后的一个节点移到dummy node之后，重复此操作知道head成为末节点为止*/

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




