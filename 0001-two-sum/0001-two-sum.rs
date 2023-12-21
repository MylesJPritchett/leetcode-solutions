use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut hm = HashMap::new();
        
        for i in 0..nums.len() {
            let needed = (target - nums[i]);
            
            if let Some(idx) = hm.get(&needed) {
               return vec![i as i32, *idx as i32];
            } else {
                hm.insert(nums[i], i);
            }
            
        }
        Vec::new()
    }
}