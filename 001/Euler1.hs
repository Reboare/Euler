isMultiple :: Int -> Bool
isMultiple n = (rem n 3 == 0) || (rem n 5 == 0)

predicate :: Int -> Int -> Int
predicate a b = if isMultiple b then a + b else a 

main :: IO ()
main = print $ foldl predicate 3 [5..999]