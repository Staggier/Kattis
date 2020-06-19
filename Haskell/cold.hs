cold :: IO ()
cold = do
    inp <- getLine
    let lst = words inp  
    putStrLn . show . length $ filter ((< 0) . read) lst
    
main = do
    inp <- getLine
    cold