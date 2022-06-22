fn fib(n: i32) -> i32 {
  if n == 0 {
    return 1;
  } else if n == 1 {
    return 2;
  } else {
    return fib(n - 1) + fib(n - 2);
  }
}

fn is_even(x: i32) -> bool {
  return x % 2 == 0;
}

fn main() {
  let mut idx: i32 = 0;
  let mut even_sum: i32 = 0;
  loop {
    let fib_item = fib(idx);

    if fib_item > 4000000 {
      break;
    }

    if is_even(fib_item) {
      even_sum += fib_item;
    }

    idx += 1;
  }
  println!("{}", even_sum);
}
