/**
* 
* @author ChenJie
* @date	Oct 6, 2018 5:53:03 PM
*/
public class RemoveElementSolution {

	public int removeElement(int[] nums, int val) {
		if(nums == null || nums.length == 0) {
			return 0;
		}
		int len = nums.length;
		int newLen = len;
		int p = 0;
		int q = len-1;
		while(p <= q) {
			while(nums[p] != val) {
				p ++;
				if(q < p) {
					break;
				}
			}
			while(nums[q] == val) {
				q --;
				newLen --;
				if(q < p) {
					break;
				}
			}
			if(p < q) {
				swap(nums, p, q);
			}
		}
		return newLen;
    }
	
	private void swap(int[] nums, int p, int q) {
		int temp = nums[p];
		nums[p] = nums[q];
		nums[q] = temp;
	}
	
	public static void main(String[] args) {
		int[] nums = {3,3};
		int val = 3;
		int len = new RemoveElementSolution().removeElement(nums, val);
		System.out.println(len);
	}
}
