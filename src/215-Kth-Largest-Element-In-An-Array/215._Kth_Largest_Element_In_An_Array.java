package leetcode;

import java.util.Comparator;
import java.util.PriorityQueue;

public class FindKthLargest_215 {
    public int findKthLargest(int[] nums, int k) {
        if(nums == null || nums.length == 0){
            return -1;
        }
        Comparator<Integer> cmp = new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o2 - o1;
            }
        };
        PriorityQueue<Integer> queue = new PriorityQueue<>(cmp);
        for(int i = 0; i < nums.length; i++){
            queue.add(nums[i]);
        }
        for(int i = 1; i < k; i++){
            queue.poll();
        }
        return queue.peek();
    }
}
