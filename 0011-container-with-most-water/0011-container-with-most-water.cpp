class Solution {
public:
    int maxArea(vector<int>& height) {
        // *min_element(height.begin(),height.end());
        int max_area = 0,i = 0;
        for( ; i < height.size(); i++){
            int area = 0;
            for(int j = i+1; j < height.size(); j++){
                area = min(height[i],height[j])*(j-i);
            }
            if(area > max_area)
                max_area = area;
        }
        return max_area;
    }
};