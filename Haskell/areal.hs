main = do
    inp <- getLine
    putStrLn $ show (4 * sqrt (read inp))