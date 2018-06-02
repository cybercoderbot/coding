class Solution {
public:
    bool isValid(string s) {
        if(s.empty()) return true;
        int n = s.size();
        if (n%2) return false;
        stack<char> t;
        set<char> opening = {'(', '[', '{'};
        set<char> closing = {')', ']', '}'};
        for (auto c : s){
            if (opening.count(c)){
                t.push(c);
            }else if(closing.count(c)){
                if(t.empty()) return false;
                auto p = t.top(); t.pop();
                if(c==')' && p!='(') return false;
                else if(c==']' && p!='[') return false;
                else if(c=='}' && p!='{') return false;
            }
        }
        return t.empty();
    }
};


class Solution {
public:
    bool isValid(string s) {
        stack<char> t;
        for (char c : s) {
            if (c == '(') stk.push(')');
            else if (c == '[') stk.push(']');
            else if (c == '{') stk.push('}');
            else {
                if (stk.empty() || stk.top() != c) return false;
                else stk.pop();
            }
        }
        return stk.empty();
    }
};