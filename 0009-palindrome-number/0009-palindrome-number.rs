impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let (mut rev, mut org) = (0, x);

        while org>0 {
            rev = (rev * 10) + org % 10;
            org /= 10;
        }

        rev == x
    }
}