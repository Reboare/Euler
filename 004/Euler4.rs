fn palindrome(x:uint) -> bool  {
    let st = str::to_chars(fmt!("%u", x));
    let rev = vec::reversed(st);
    rev == st
}

fn main() {
    let mut maximum = 0;
    for uint::range(100,1000) |x| {
        for uint::range(100, 1000) |y| {
            let j = x * y;
            if palindrome(j) && j > maximum{
                maximum = j;
            }
        }
        
    }
    io::println(fmt!("%u", maximum));
}