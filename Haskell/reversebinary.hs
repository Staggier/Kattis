import Data.Digits (digits, unDigits)

convertBase :: Integral a => a -> a -> [a] -> [a]
convertBase from to = digits to . unDigits from

rb :: Int -> Int
rb n = unDigits 10 (convertBase 2 10 [unDigits 2 (reverse $ convertBase 10 2 [n])])

main :: IO ()
main = do
    inp <- getLine
    let n = read inp
    putStrLn . show $ rb n