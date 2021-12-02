use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn day1() -> i32 {
    let mut last: i32 = 0;
    let mut increases: i32 = 0;
    if let Ok(lines) = read_lines("./src/day1.txt") {
        for line in lines {
            if let Ok(distance) = line {
                let int: i32 = distance.parse().unwrap();
                if last != 0 {
                    if int > last {
                        increases += 1;
                    }
                }
                last = int;
            }
        }
    }
    increases
}

fn main() {
    println!("{}", day1())
}
