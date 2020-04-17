extern crate clap;

use clap::{Arg, App};

fn main() {
    let matches = App::new("marbleextractor")
        .version("0.1.0")
        .author("Collin Allen <collin@command-tab.com>")
        .about("Extracts the marble.bza archive from Marble Blast Ultra on Xbox Live Arcade")
        .arg(Arg::with_name("file")
            .short("f")
            .long("file")
            .takes_value(true)
            .help("The path to marble.bza"))
        .get_matches();

    let bza = matches.value_of("file").unwrap_or("input.txt");
    println!("Extracting {}", bza);
}
