package Easy.GroupAnagrams.MoveZeroes;

public class MoveZeroes {

    public void moveZeroes(int[] nums) {
        int n = nums.length;
        int curr0 = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] != 0) {
                swap(nums, curr0++, i);
            }
        }
    }
    public void swap(int[] nums, int from, int to) {
        int temp = nums[to];
        nums[to] = nums[from];
        nums[from] = temp;
    }
}
