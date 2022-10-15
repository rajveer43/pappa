//33. Search in Rotated Sorted Array

class Solution{
    public:
    int search(vector<int>& nums, int target){
        int n = nums.size();
        if(n == 0) return -1;
        int l = 0, r = n - 1;
        while(l < r){
            int mid = l + (r - l) / 2;
            if(nums[mid] == target) return mid;
            if(nums[l] < nums[mid]){
                if(nums[l] <= target && target < nums[mid]) r = mid - 1;
                else l = mid + 1;
            }else if(nums[l] > nums[mid]){
                if(nums[mid] < target && target <= nums[r]) l = mid + 1;
                else r = mid - 1;
            }else l++;
        }
        if(nums[l] == target) return l;
        return -1;

    }
}