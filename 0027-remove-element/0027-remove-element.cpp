class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0; // This pointer will keep track of the position for the next non-`val` element

        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] != val) {
                nums[k] = nums[i];
                k++;
            }
        }
        return k; // k now represents the number of elements that are not equal to `val`
    }
};