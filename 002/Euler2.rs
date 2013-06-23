fn main(){
    let mut summation = 0u;

    let mut first = 1u;
    let mut second = 1u;
    while second < 4000000 {
        if second % 2 == 0{summation += second};
        second = first + second;
        first = second - first;
    }
    io::println(fmt!("%u", summation))
}