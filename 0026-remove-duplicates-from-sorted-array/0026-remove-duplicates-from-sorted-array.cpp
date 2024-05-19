class Solution {
public:
    int removeDuplicates(vector<int>& nums) {

        if (nums.empty()) {
            return 0;
        }
        
        int uniqueIndex = 1; // Start from the second element
        
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] != nums[i - 1]) { // Compare with the previous element
                nums[uniqueIndex] = nums[i]; // Move the unique element forward
                ++uniqueIndex; // Increment the position for the next unique element
            }
        }
        
        return uniqueIndex; // The length of the array with unique elements
        
    }
};