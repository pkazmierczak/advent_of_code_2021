{-# LANGUAGE OverloadedStrings #-}

import Data.Text (pack, splitOn, unpack)
import System.IO

-- |condSum will return a sum of all second elements of a list of tuples given
-- the first tuple element matches the string
condSum :: (Num a1, Eq a2) => a2 -> [(a2, a1)] -> a1
condSum string tuples =
    sum $ map snd $ filter (\x -> fst x == string) tuples

computeCoordinates :: [(String, Int)] -> (Int, Int)
computeCoordinates lineTuples = (x, y)
  where
    x = condSum "forward" lineTuples
    y = condSum "down" lineTuples - condSum "up" lineTuples

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