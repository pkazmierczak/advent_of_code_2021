{-# LANGUAGE OverloadedStrings #-}

import Control.Arrow ((&&&))
import Data.List (group, sort)
import Data.Text (pack, splitOn, unpack)
import System.IO

joinHead ([] : _) = []
joinHead xs = map head xs

--Takes the list of binary strings and "flips" them by constructing lists of
--each elements
vertical ([] : _) = []
vertical ([x] : xs) = [joinHead ([x] : xs)]
vertical xs = joinHead xs : vertical (map tail xs)

--couldn't figure out how to implement this. I found this magical answer
--https://stackoverflow.com/a/62010996/609972 but don't really understand how
--Control.Arrow works... This really motivates me to read more abouto arrows
--though.
mostCommon = snd . maximum . map (length &&& head) . group . sort
leastCommon = snd . minimum . map (length &&& head) . group . sort

bintodec 0 = 0
bintodec i = 2 * bintodec (div i 10) + mod i 10

main :: IO ()
main = do
  inh <- openFile "day03.txt" ReadMode
  contents <- hGetContents inh -- gets a handle and returns a string
  let lines = splitOn "\n" (pack contents)
  let gamma = map mostCommon (vertical (map unpack lines))
  let epsilon = map leastCommon (vertical (map unpack lines))
  print (bintodec (read epsilon ::Int) * bintodec (read gamma ::Int))

  hClose inh