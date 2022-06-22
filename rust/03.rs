
fn is_prime(x: i32) -> bool {
    for div in 2..((x as f32).sqrt() as i32) {
        if x % div == 0 {
            return false;
        }
    }
    return true;
}


fn main() {
    let number: i64 = 600851475143;
    let mut div = (number as f64).powf(0.5) as i64;

    loop {
        if div <= 0 {
            break;
        }

        if is_prime(div as i32) && number % div == 0 {
            println!("{}", div);
            break;
        }

        div -= 1;
    }
}
