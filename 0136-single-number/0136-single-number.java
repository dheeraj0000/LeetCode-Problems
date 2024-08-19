class Solution {
    public int singleNumber(int[] nums) {
        int unique=0;
        for(int i=0;i<=nums.length-1;i++)
        {
            unique=unique^nums[i];
        }
        return unique;
    }
}