
fn main() {
  let mut total_sum: i32 = 0;

  for i in 0..1000 {
    if i % 3 == 0 || i % 5 == 0 {
      total_sum += i;
    }
  }

  println!("{}", total_sum);
}

