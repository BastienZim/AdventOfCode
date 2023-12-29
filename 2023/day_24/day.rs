use std::fs::read_to_string;
use std::path::Path;

fn main() {
    //    read_file(true);

    let lines = read_lines(false);
    
    for line in lines {
    }
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
