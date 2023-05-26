# leetcode

## 1. 217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

## Example 1:
Input: nums = [1,2,3,1]
Output: true

## Example 2:
Input: nums = [1,2,3,4]
Output: false

## Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

## Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109

## O(n^2) solution :
```cpp
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        for (auto i = nums.begin();i<nums.end();i++){
            for (auto j = nums.begin();j<nums.end();j++){
                if(i != j)
                    if(*i == *j)
                        return true;
            }
        }
        return false;
    }
};
```

## Faster than brute force

'''cpp
// Sorted Approach takes less time than the above and is accepted by leetcode
class Solution {
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
'''