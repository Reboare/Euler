main = do
    x <- readFile "Euler13.txt"
    putStrLn $ (take 10).show $ sum (map (\x -> read x :: Integer) (lines x))