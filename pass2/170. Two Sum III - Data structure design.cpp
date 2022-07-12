class TwoSum {
public:
    void add(int number) {
        m[number]++;
    }
    bool find(int value) {
        for (auto v : m) {
            int diff = value - v.first;
            if ((diff != v.first && m.count(diff)) || (diff == v.first && v.second > 1)) {
                return true;
            }
        }
        return false;
    }
private:
    unordered_map<int, int> m;
};