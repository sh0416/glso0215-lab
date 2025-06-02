use std::io;
mod solution_10870;
fn main(){
	assert_eq!(solution_10870::fibonacci(0), 0);
	assert_eq!(solution_10870::fibonacci(1), 1);
	assert_eq!(solution_10870::fibonacci(5), 5);
	assert_eq!(solution_10870::fibonacci(10), 55);
	println!("0, 1, 5, 10의 test case에 대해 성공");
}