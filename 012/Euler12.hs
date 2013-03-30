import Data.List.Split

gridConversion xs = map (\x -> map (\y -> read y :: Int) x ) lined
    where
        lined = map (splitOn " ") (lines xs)

permutationRule y x = undefined


main = print $ gridConversion "23 34\n45 46"