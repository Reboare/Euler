palindrome :: Int -> Bool
palindrome x = 
    let 
        str = show x
    in 
        str == reverse str

main :: IO ()
main = print $ maximum $ filter palindrome [x*y| x <- [100..999], y <- [100..999]]