import Data.Char (ord)
import Data.Bits (xor)
import Data.List.Split
import Data.List

chars = map ord "abcdefghijklmnopqrstuvwxyz"

possibles :: [[Int]]
possibles = concat [[[x,y,z], [x, z, y], [z, y, x], [z, x, y], [y, x, z], [y, z,  x]] | x <- chars, y <- chars, z <- chars]

decrypt :: [Int] -> [Int] -> [Int]
decrypt xs ys = map (\(x, y) -> x `xor` y) (zip xs ys)

keys :: [[Int]] -> [[Int]]
keys xs = map (\x -> take (length xs) (cycle x)) possibles

numOf :: (Eq a) => a -> [a] -> Int
numOf a xs = length $! elemIndices a xs

spaceSort zs = sortBy predicate zs
    where
        predicate xs ys | (numOf 32 xs) < (numOf 32 ys) = GT
                        | (numOf 32 xs) > (numOf 32 ys) = LT 
                        | otherwise = EQ

main = do
    xs <- readFile "Euler59.txt"
    let toList = map (\x -> read x :: Int) (splitOn "," xs)
    let sp = take 10 $ spaceSort $ map (decrypt toList) (keys possibles)
    print $ length $ filter (\x -> length x == 3) (subsequences chars)