
coins :: [Int]
coins = [1,2,5,10,20,50,100,200]

partition :: Int -> Int
partition n = 1 + sum (map (\x -> partition (n-x)) [1..(n `quot` 2)])

main = print $ (partition 200)