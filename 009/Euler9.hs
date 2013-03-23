euclidGen m n | m > n = []
              | otherwise =  [abs(m^2 - n^2), 2*m*n, m^2+n^2]

genEuclids = filter ((/=) []) [euclidGen x y | x <- [1..20], y<- [1..20]]

ridTriplets = head $ filter (\x -> sum x == 1000) genEuclids

main = print $ product ridTriplets