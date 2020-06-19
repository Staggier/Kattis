import Data.List (isInfixOf)

deathknight :: IO ()
deathknight = do
    trash <- getLine
    inp <- getContents
    let games = lines inp
    putStrLn $ show . length $ filter (not . isInfixOf "CD") games
    
main = deathknight