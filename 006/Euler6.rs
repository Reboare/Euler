fn main() {
    //Would rather use foldl but got lazy
    let mut square_sum = 0;
    let mut sum_square = 0;
    for uint::range(1,101) |n| {
        square_sum += n*n;
        sum_square += n;
    }
    io::println(fmt!("%u", sum_square*sum_square - square_sum))
}