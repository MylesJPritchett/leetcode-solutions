struct MinStack {
    stack: Vec<i32>,
    min_stack: Vec<i32>,
}

use std::cmp::{min};
/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MinStack {

    fn new() -> Self {
        MinStack {
            stack: Vec::new(),
            min_stack: Vec::new(),
        }
    }
    
    fn push(&mut self, mut val: i32) {
        self.stack.push(val);
        if self.min_stack.len() > 0 {
            val = min(val, self.get_min());
        }
        self.min_stack.push(val);
    }
    
    fn pop(&mut self) {
        self.stack.pop();
        self.min_stack.pop();
    }
    
    fn top(&self) -> i32 {
        self.stack.last().cloned().unwrap()
    }
    
    fn get_min(&self) -> i32 {
        self.min_stack.last().cloned().unwrap()
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * let obj = MinStack::new();
 * obj.push(val);
 * obj.pop();
 * let ret_3: i32 = obj.top();
 * let ret_4: i32 = obj.get_min();
 */