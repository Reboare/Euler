euclidGen :: Int -> Int -> [Int]
euclidGen m n | m > n = []
              | otherwise =  [abs(m*m - n*n), 2*m*n, m*m+n*n]

genEuclids :: [[Int]]
genEuclids = filter ([] /=) [euclidGen x y | x <- [1..20], y<- [1..20]]

ridTriplets :: [Int]
ridTriplets = head $ filter (\x -> sum x == 1000) genEuclids

main :: IO ()
main = print $ product ridTriplets