use std::fs::read_to_string;
use std::path::Path;

fn main() {
    //    read_file(true);

    let lines = read_lines(true);
    let mut v: Vec<i32> = Vec::new();
    let valid_digits: [&str; 10] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"];

    for line in lines {
        let mut is_first = true;
        let mut first_number = char::default();
        let mut last_number = char::default();

        for elt in line.chars() {
            if elt.is_numeric() {
                if is_first {
                    first_number = elt;
                    is_first = false;
                } else {
                    last_number = elt;
                }
            }
        }


        let n_digits = count_digits(line.clone());

        let mut a_string = String::from("");
        a_string.push(first_number);
        if n_digits == 1 {
            a_string.push(first_number);
        } else {
            a_string.push(last_number);
        }
        let my_int: i32 = a_string.parse().unwrap();
        v.push(my_int);
    }
    let sum: i32 = v.iter().sum();
    println!("{}", sum)
}

fn count_digits(line: String) -> i32 {
    let mut counter: i32 = 0;
    for elt in line.chars() {
        if elt.is_numeric() {
            counter += 1;
        }
    }
    counter
}

fn read_lines(example: bool) -> Vec<String> {
    let file_path = if example {
        Path::new("./example_in.txt")
    } else {
        Path::new("./input.txt")
    };

    read_to_string(file_path)
        .unwrap() // panic on possible file-reading errors
        .lines() // split the string into an iterator of string slices
        .map(String::from) // make each slice into a string
        .collect() // gather them together into ,a vector
}
