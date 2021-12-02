{-# LANGUAGE OverloadedStrings #-}

import Data.Text (pack, splitOn, unpack)
import System.IO

computeCoordinates :: [(String, Int)] -> (Int, Int)
computeCoordinates lineTuples = (x, y)
  where
    x = sum $ map snd $ filter (\x -> fst x == "forward") lineTuples
    y =
      sum (map snd $ filter (\x -> fst x == "down") lineTuples)
        - sum (map snd $ filter (\x -> fst x == "up") lineTuples)

main :: IO ()
main = do
  inh <- openFile "day02.txt" ReadMode
  contents <- hGetContents inh -- gets a handle and returns a string
  let lines = splitOn "\n" (pack contents)

  -- make them into tuples of (direction, distance) for easier processing
  let lineTuples = map (\[x, y] -> (unpack x, read $ unpack y)) (splitOn " " <$> lines)

  let finalCoordinates = computeCoordinates lineTuples
  print (uncurry (*) finalCoordinates)

  hClose inh