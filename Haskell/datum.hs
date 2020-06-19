datum :: Int -> Int -> String
datum n k = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"] !! ((n + (sum (take (k - 1) [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])) - 1) `mod` 7)

main :: IO ()
main = do
    inp <- getLine
    let lst = map read $ (words inp)
    putStrLn $ datum (lst !! 0) (lst !! 1)