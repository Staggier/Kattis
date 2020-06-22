f :: Integral n => n -> n
f n = product [1..n]

lfd :: Integral n => n -> n
lfd x = f x `mod` 10

putLst :: IO ()
putLst = do
    inp <- getContents
    let lst = map read $ lines inp
    mapM_ putStrLn $ map (show . lfd) lst
    
main = do
    trash <- getLine
    putLst
