--{-#LANGUAGE BangPatterns#-}
newSeq :: Integer -> Integer
newSeq n
    | r == 0 = q
    | otherwise = (+) 1 $! (3 * n)
    where (q, r) = quotRem n 2

lenSeq :: Integer -> Integer
lenSeq 1 = 1
lenSeq n = (+) 1 $! lenSeq $! newSeq n 

longest :: (Integer, Integer) -> [Integer] -> Integer
longest (a, _) [] = a
longest (a, n) (x:xs) | newLen > n = longest (x, newLen) xs
                      | otherwise = longest (a, n) xs
                        where
                            newLen = lenSeq x

main:: IO ()
main = print $ longest (1, 1) [2..10000]

