check :: String -> String -> String
check a b
  | la < lb = "<"
  | la > lb = ">"
  | otherwise = cmpr ca cb
  where
    ca' = dropWhile (=='0') a
    cb' = dropWhile (=='0') b
    ca = if ca' == [] then "0" else ca'
    cb = if cb' == [] then "0" else cb'
    la = length ca
    lb = length cb
    cmpr [] [] = "="
    cmpr (x:xs) (y:ys)
      | x < y = "<"
      | x > y = ">"
      | otherwise = cmpr xs ys

main :: IO ()
main = do
  a <- getLine
  b <- getLine
  putStrLn $ check a b
