minus (x:xs) (y:ys) = case (compare x y) of 
          LT -> x : minus  xs  (y:ys)
          EQ ->     minus  xs     ys 
          GT ->     minus (x:xs)  ys
minus  xs     _     = xs
union (x:xs) (y:ys) = case (compare x y) of 
          LT -> x : union  xs  (y:ys)
          EQ -> x : union  xs     ys 
          GT -> y : union (x:xs)  ys
union  xs     ys    = xs ++ ys
-- |From http://en.literateprograms.org/Sieve_of_Eratosthenes_(Haskell)
primesTME = 2 : ([3,5..] `minus` unionAll [[p*p,p*p+2*p..] | p <- primes']) 
 where
   primes' = 3 : ([5,7..] `minus` unionAll [[p*p,p*p+2*p..] | p <- primes'])   
   unionAll ((x:xs):t) = x : union xs (unionAll (pairs t))
   pairs ((x:xs):ys:t) = (x : union xs ys) : pairs t 

isPrime x  = primeFilter x primesTME
    where
        primeFilter z (l:s) | l > z  = False
                            | l < z  = primeFilter z s
                            | l == z = True 

squares = [2 * (x^2) | x <- [1..]]

composite = filter (\x -> not (isPrime x)) [3,5..]

conjecture x = elem True (map isPrime (map (x -) (takeWhile (x >) squares)))

main = print $ head $ filter (\x -> not $ conjecture x) composite