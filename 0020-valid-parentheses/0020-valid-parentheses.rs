impl Solution {
    fn is_valid(s: String) -> bool {
    let mut stack: Vec<char> = Vec::new();

    for c in s.chars() {
        if c == '(' || c == '[' || c == '{' {
            // Push the open bracket onto the stack
            stack.push(c);
        } else {
            // If the stack is empty, the string is not valid
            if stack.is_empty() {
                return false;
            }

            // Check the type of the open bracket at the top of the stack
            let top = stack[stack.len() - 1];
            if (c == ')' && top == '(') || (c == ']' && top == '[') || (c == '}' && top == '{') {
                // If it matches the type of the closing bracket, pop it off the stack
                stack.pop();
            } else {
                // If it doesn't match, the string is not valid
                return false;
            }
        }
    }

    // If the stack is empty at the end, the string is valid
    return stack.is_empty();
}

}