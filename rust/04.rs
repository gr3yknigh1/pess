
fn abs(x: i32) -> u32 {
    return if x > 0 { x as u32 } else { -x as u32 };
}


fn digit(x: i32, idx: u32) -> u32 {
    let x: u32 = abs(x);
    return (x % (10_u32.pow(idx + 1)) - (x % 10_u32.pow(idx))) / 10_u32.pow(idx);
}


fn length(x: i32) -> u32 {
    let mut x = abs(x);
    let mut ln: u32 = 1;
    while x > 1 {
        x /= 10_u32;
        ln += 1;
    }
    return ln;
}

fn is_even(x: i32) -> bool {
    return x % 2 == 0;
}

fn is_palindrome(x: i32) -> bool{
    let ln = length(x);
    let mut head = 0;
    let mut tail = ln - 2;
    let mut is_palindorme = true;
    while head < ln / 2 + 1 || tail > ln / 2{
        if digit(x, head) != digit(x, tail) {
            is_palindorme = false;
            break;
        }
        head += 1;
        tail -= 1;
    }
    return is_palindorme;
}

fn max(a: i32, b: i32) -> i32 {
    return if a > b { a } else { b }
}


fn main() {
    let mut mx_palindrome = 0;
    for i in 100..1000 {
        for j in 100..1000 {
            let num = j * i;
            if is_palindrome(num) {
                mx_palindrome = max(mx_palindrome, num);
            }
        }
    }
    println!("{}", mx_palindrome);
}
