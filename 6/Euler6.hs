main :: IO ()
main = print $ sum [1..100] ^ 2 -  sum (map (\x -> x^2) [1..100])