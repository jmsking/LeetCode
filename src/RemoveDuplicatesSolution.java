/**
* 
* @author ChenJie
* @date	Oct 1, 2018 10:03:53 PM
*/
public class RemoveDuplicatesSolution {

	public int removeDuplicates(int[] nums) {
		if(nums == null || nums.length == 0) {
			return 0;
		}
		if(nums.length == 1) {
			return 1;
		}
		int len = nums.length;
		int currLen = len;
		int iter = 1;
		int p = 0;
		int q = 1;
		while(iter < len) {
			int moveStep = q - p - 1;
			if(nums[q] != nums[p] && moveStep == 0) {
				p++;
				q++;
			}
			else if(nums[q] != nums[p] && moveStep > 0) {
				for(int k = q; k < currLen; k ++) {
					nums[k-moveStep] = nums[k];
				}
				currLen -= moveStep;
				p ++;
				q = p+1;
			}
			else if(nums[q] == nums[p]) {
				q ++;
			}
			iter ++;
		}
		if(q - p > 1) {
			currLen -= (q-p-1);
		}
        return currLen;
    }
	
	public static void main(String[] args) {
		int nums[] = {1, 1, 2, 2, 2, 3, 3, 3, 3};
		int len = new RemoveDuplicatesSolution().removeDuplicates(nums);
		System.out.println(len);
	}
	
}
