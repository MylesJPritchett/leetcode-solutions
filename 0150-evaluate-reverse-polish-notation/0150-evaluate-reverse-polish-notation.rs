impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack = Vec::new();
        
        for token in tokens {
            if let Ok(num) = token.parse::<i32>(){
                stack.push(num);
            } 
            else {
                if let (Some(num2), Some(num1)) = (stack.pop(), stack.pop()){
                    match token.as_str() {
                       "+" => { stack.push(num1 + num2) },
                       "-" => { stack.push(num1 - num2)  },
                       "*" => { stack.push(num1 * num2)  },
                       "/" => { stack.push(num1 / num2)  },
                        _ => (),
                    }
                }
        
                else {
                    return 0;
                }
                
               
            }
        }
        *stack.last().unwrap()
    }
}