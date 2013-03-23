genFib :: [Integer]
genFib = 1:1:zipWith (+) genFib (tail genFib)

evenGenFib :: [Integer]
evenGenFib = filter even genFib

main :: IO ()
main = print.sum $ takeWhile (<= 4000000) evenGenFib