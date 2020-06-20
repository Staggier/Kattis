import Data.List (intercalate)

bijele :: IO ()
bijele = do
    inp <- getLine
    putStrLn . intercalate " " $ map show $ zipWith (-) [1, 1, 2, 2, 2, 8] (map read $ (words inp))

main :: IO ()
main = bijele