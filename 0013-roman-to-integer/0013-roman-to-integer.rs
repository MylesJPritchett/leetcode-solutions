use std::collections::HashMap;

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let mut roman_numeral: HashMap<char, i32> = HashMap::from([
    ('I', 1),
    ('V', 5),
    ('X', 10),
    ('L', 50),
    ('C', 100),
    ('D', 500),
    ('M', 1000),
]);
        
        let mut sum: i32 = 0;
        
        let mut prev: i32 = 0;
        
        for char in s.to_uppercase().chars().rev() {
            if let Some(num) = roman_numeral.get(&char) {
                if *num < prev {
                    sum -= num;
                } else {
                    sum += num;
                }
                prev = *num;
            } else {
                panic!("Contains non-roman number [{}]", char)
            }
        }
        sum
    }
}