batterup:: IO ()
batterup = do
    inp <- getLine
    let lst = filter (> -1) . map read $ (words inp)   
    putStrLn . show $ ((fromIntegral . sum) lst) / ((fromIntegral . length) lst)

main :: IO ()
main = do
    inp <- getLine
    batterup