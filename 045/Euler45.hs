hex :: [Integer]
hex = map (\n -> n * (2*n - 1)) [144..]

pen :: [Integer]
pen = map (\n -> n * (3*n - 1) `quot` 2) [166..]

sortedDup :: (Eq a, Ord a) => [a] -> [a] -> a
sortedDup (x:xs) (y:ys) | x > y = sortedDup (x:xs) ys
                         | x < y = sortedDup xs (y:ys)
                         | x == y = x

main = print $ sortedDup hex pen