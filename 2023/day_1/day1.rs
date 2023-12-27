use std::fs::read_to_string;
use std::path::Path;

fn main() {
    //    read_file(true);

    let lines = read_lines(false);
    let mut v: Vec<i32> = Vec::new();
    let valid_digits: [&str; 20] = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "0", "1",
        "2", "3", "4", "5", "6", "7", "8", "9",
    ];
    let valid_digits_asint: [char; 20] = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7',
        '8', '9',
    ];

    for line in lines {
        let mut first_index = line.chars().count() + 1;
        let mut last_index: usize = 0;
        let mut first_number = char::default();
        let mut last_number = char::default();
        let mut counter: i8 = 0;

        for (i, x) in valid_digits.iter().enumerate() {
            if line.contains(x) {
                let mut index = line.find(x).unwrap_or(0);
                counter += 1;
                if index <= first_index {
                    first_index = index;
                    first_number = valid_digits_asint[i]
                }
                if index + x.chars().count() <= line.chars().count() {
                    let mut slice = &line[index + x.chars().count()..];
                    let last_index_counter = index;
                    while slice.contains(x) {
                        let new_cut_index = slice.find(x).unwrap_or(0);
                        index = new_cut_index + last_index_counter;
                        slice = &slice[new_cut_index + x.chars().count()..];
                    }
                }
                if last_index <= index {
                    last_index = index;
                    last_number = valid_digits_asint[i]
                }
            }
        }

        //        println!("{first_number}{last_number}");
        //let n_digits = count_digits(line.clone());
        println!("{first_number}{last_number}");
        let mut a_string = String::from("");
        a_string.push(first_number);
        assert!(counter != 0);
        if counter == 1 {
            a_string.push(first_number);
        } else {
            a_string.push(last_number);
        }
        //println!("{}\n", a_string);
        let my_int: i32 = a_string.parse().unwrap();
        v.push(my_int);
    }
    let sum: i32 = v.iter().sum();
    println!("{}", sum)
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
