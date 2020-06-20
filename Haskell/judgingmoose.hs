moose :: Int -> Int -> IO ()
moose 0 0 = putStrLn "Not a moose"
moose n k = putStrLn $ (if n == k then "Even " else "Odd ") ++ (show $ if n > k then n * 2 else k * 2)

main :: IO ()
main = do
    inp <- getLine
    let lst = map read $ (words inp)
    moose (lst !! 0) (lst !! 1)
    