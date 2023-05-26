#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (auto i = nums.begin(); i < nums.end() - 1; i++) {
            if (*i == *(i + 1)) {
                return true;
            }
        }
        return false;
    }
};

// Sorted Approach takes less time than the above and is accepted by leetcode
class Solution1 {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        bool flag = false;
        for(int i =0;i<nums.size()-1;i++){
            if(nums[i] == nums[i+1]) return true;
        }
        return flag;
    }
};

class Solution2 {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> numSet;
        for (int num : nums) {
            if (numSet.count(num) > 0) {
                return true;
            }
            numSet.insert(num);
        }
        return false;
    }
};


int main() {
    Solution2 s;
    vector<int> v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    v.push_back(4);
    v.push_back(5);
    if (!v.empty() && !s.containsDuplicate(v)) {
        cout << "No duplicates";
    }
    return 0;
}
