{-# LANGUAGE OverloadedStrings #-}

import Data.Text (pack, splitOn, unpack)
import System.IO

joinHead ([] : _) = []
joinHead xs = map head xs

--Takes the list of binary strings and "flips" them by constructing lists of
--each elements
vertical ([] : _) = []
vertical ([x] : xs) = [joinHead ([x] : xs)]
vertical xs = joinHead xs : vertical (map tail xs)

count x = length . filter (== x)

mostCommon xs
  | count '1' xs > count '0' xs = '1'
  | otherwise = '0'

leastCommon xs
  | count '1' xs < count '0' xs = '1'
  | otherwise = '0'

bintodec 0 = 0
bintodec i = 2 * bintodec (div i 10) + mod i 10

main :: IO ()
main = do
  inh <- openFile "../day03.txt" ReadMode
  contents <- hGetContents inh -- gets a handle and returns a string
  let lines = splitOn "\n" (pack contents)
  let gamma = map mostCommon (vertical (map unpack lines))
  let epsilon = map leastCommon (vertical (map unpack lines))
  print (bintodec (read epsilon :: Int) * bintodec (read gamma :: Int))

  hClose inh