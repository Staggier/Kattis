romans :: Double -> Int
romans n = round $ n * 1000 * 5280/4854

main :: IO ()
main = do
    inp <- getLine
    putStrLn . show $ romans (read inp)