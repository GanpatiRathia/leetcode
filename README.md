# leetcode

## 1. Two Sum - Easy
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Example 1:
Input: nums = [2,7,11,15], target = 9

Output: [0,1]

Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

## Example 2:
Input: nums = [3,2,4], target = 6

Output: [1,2]

## Example 3:
Input: nums = [3,3], target = 6

Output: [0,1]

## Constraints:
2 <= nums.length <= 104

-109 <= nums[i] <= 109

-109 <= target <= 109

Only one valid answer exists.

## Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?

## O(n^2) solution :
'''cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        for(auto it1= nums.begin();it1 != nums.end(); ++it1 ){
            for(auto it2 = it1+1; it2!=nums.end(); ++it2){
                if(*it2 == target - *it1){
                    result.push_back(it1 - nums.begin());
                    result.push_back(it2 - nums.begin());
                    return result;
                }
            }
        }
        return{};
    }
};
'''