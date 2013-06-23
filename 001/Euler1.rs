fn main() {
    let mut summation : uint = 0u;
    for uint::range(1, 1000) |n| {
        if n % 3 == 0 || n % 5 == 0 { summation += n }
    }
    io::println(fmt!("%u" ,summation)); 
}
