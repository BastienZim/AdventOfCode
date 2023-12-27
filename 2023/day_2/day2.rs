use std::collections::HashMap;
use std::fs::read_to_string;
use std::path::Path;

fn main() {
    //    read_file(true);

    let lines = read_lines(false);

    let mut _possible_games: Vec<i32> = Vec::new();
    let mut all_powers: Vec<i32> = Vec::new();
    let mut requirements = HashMap::new();
    requirements.insert(String::from("red"), 12);
    requirements.insert(String::from("green"), 13);
    requirements.insert(String::from("blue"), 14);

    for l in lines {
        let mut _max_cubes: HashMap<String, i32> = HashMap::new();
        let mut game: Vec<&str> = l.split("Game ").collect();
        game = game[1].split(":").collect(); //&l[5..];

        let _game_num: i32 = game[0].parse().unwrap();

        let gamestr = game[1].replace(";", ","); //No idea how to avoid this
        game = gamestr.split(",").collect();

        let cubes: Vec<_> = game
            .iter()
            .map(|a| a.split(" ").collect::<Vec<_>>())
            .collect();

        for c in cubes {
            let color: String = c[2].to_string();
            let numberofcolor: i32 = c[1].parse().unwrap();
            if _max_cubes.contains_key(&color) {
                if _max_cubes.get(&color) < Some(&numberofcolor) {
                    _max_cubes.insert(color, numberofcolor);
                }
            } else {
                _max_cubes.insert(color, numberofcolor);
            }
        }
        let mut power: i32 = 1;
        for v in _max_cubes.values() {
            power *= v
        }
        all_powers.push(power);
        //println!("\nREQUIREMENTS: {:?}", requirements);
        //println!("MAX cubes re: {:?}", _max_cubes);
        if requirements
            .keys()
            .into_iter()
            .all(|k| _max_cubes.contains_key(k))
        {
            if requirements
                .clone()
                .into_iter()
                .all(|(k, v)| _max_cubes.get(&k) <= Some(&v))
            {
                //println!("OK game {}", _game_num)
                _possible_games.push(_game_num)
            }
        }
    }

    let sum_part1: i32 = _possible_games.iter().sum();
    let sum_part2: i32 = all_powers.iter().sum();
    println!("PART 1: {}", sum_part1);
    println!("PART 2: {}", sum_part2);
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
