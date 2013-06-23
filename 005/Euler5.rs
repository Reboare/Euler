fn main(){
    io::println(fmt!("%u", euler5()))

}

fn euler5() -> uint {
    let mut accum = 20;
    loop {
        for vec::each([11u, 13u, 14u, 16u, 17u, 18u, 19u]) |&n| {
            if accum % n != 0 { break; } 
            else if n == 19u{ return accum; }
        }
        accum += 20;
    }
}