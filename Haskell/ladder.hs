ladder :: IO ()
ladder = do
    inp <- getLine
    let lst = map read $ (words inp)
    putStrLn . show $ ceiling $ (lst !! 0) / (sin $ (lst !! 1) * pi/180)
    
main :: IO ()
main = ladder