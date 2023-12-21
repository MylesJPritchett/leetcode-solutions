impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        let mut result = Vec::new();
        let mut stack = Vec::new();
        
        fn backtrack(opened: i32, closed: i32, n: i32, result: &mut Vec<String>, stack: &mut Vec<&str>){
            if opened == n && closed == n {
                result.push(stack.join(""));
                return
            }
            
            if opened < n {
                stack.push("(");
                backtrack(opened + 1, closed, n, result, stack);
                stack.pop();
            }
                
            if closed < opened{
                stack.push(")");
                backtrack(opened, closed + 1, n, result, stack);
                stack.pop();
            }
            
        }
        backtrack(0, 0, n, &mut result, &mut stack);
        return result;
    }
}
