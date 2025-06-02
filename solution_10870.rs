pub fn fibonacci(n: u32) -> u32 {
    if n == 0 {
        return 0;
    } else if n == 1 {
        return 1;
    }

    let mut a = 0;
    let mut b = 1;

    for _ in 2..=n {
        let temp = a + b;
        a = b;
        b = temp;
    }
    b
}

use std::io;
fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let n: u32 = input.trim().parse().unwrap();

    let result = fibonacci(n);
    println!("{}", result);
}
