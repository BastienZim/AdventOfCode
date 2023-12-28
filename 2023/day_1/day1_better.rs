use std::fs::read_to_string;
use std::path::Path;

fn main() {
    let file_path = Path::new("./example_in.txt");
    //let file_path = Path::new("./input.txt");
    let input :&str = &read_to_string(file_path).expect("Failed to read file").to_string();

    solve2(input);
}

pub fn solve(input: Vec<String>) {
    // iterate over each line and get the two digits in the string
    let ans: u32 = input
        .into_iter()
        .map(|line| {
            let mut chars = line.chars().filter(|c| c.is_digit(10));
            // if there is no last, then double the first char
            let first = chars
                .next()
                .expect("the line should have at least one digit");
            let num = match chars.last() {
                Some(last) => format!("{}{}", first, last),
                None => format!("{}{}", first, first),
            };
            num.parse::<u32>().unwrap()
        })
        .sum();
    println!("Answer: {}", ans)
}

pub fn solve2(input: &str) {
    let ans = input
        .lines()
        .map(|line| get_number_from_line(line))
        .sum::<u32>();
    println!("Answer: {}", ans);
}

#[derive(Debug, PartialEq)]
struct NumberPosition {
    number: u32,
    position: usize,
}

fn find_digits(line: &str) -> Vec<NumberPosition> {
    line.chars()
        .enumerate()
        .filter(|(_, c)| c.is_digit(10))
        .map(|(i, c)| NumberPosition {
            number: c.to_digit(10).unwrap(),
            position: i,
        })
        .collect()
}

fn find_spelled_numbers(line: &str) -> Vec<NumberPosition> {
    let spelled_numbers = vec![
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    ];
    let mut positions: Vec<NumberPosition> = Vec::new();
    for spelled_number in spelled_numbers.clone() {
        let mut start = 0;
        while let Some(position) = line[start..].find(spelled_number) {
            positions.push(NumberPosition {
                number: spelled_numbers
                    .iter()
                    .position(|&n| n == spelled_number)
                    .unwrap() as u32
                    + 1,
                position: start + position,
            });
            start += position + spelled_number.len();
        }
    }
    positions.sort_by_key(|np| np.position);
    positions
}

fn get_number_from_line(line: &str) -> u32 {
    let digits = find_digits(line);
    let spelled_numbers = find_spelled_numbers(line);

    //println!("AAAAAAAAAA{:?}", spelled_numbers);
    let mut numbers: Vec<NumberPosition> = digits;
    numbers.extend(spelled_numbers);
    numbers.sort_by_key(|np| np.position);

    let first = numbers
        .first()
        .expect("There should be at least one number");
    let last = numbers.last().expect("There should be at least one number");
    let answer = first.number * 10 + last.number;

   // println!("{} -> {:?} + {:?} = {}", line, first, last, answer);
    answer
}
