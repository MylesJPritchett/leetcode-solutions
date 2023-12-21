impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        let (mut one_step, mut two_step) = (1, 1);
        for i in 0..n - 1 {
            let temp_variable = one_step;
            one_step = one_step + two_step;
            two_step = temp_variable;
        }
        return one_step
    }
}