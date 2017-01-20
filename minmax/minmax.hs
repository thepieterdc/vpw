module Main where
import System.IO
import Control.Monad (liftM)

leesRijen :: Int -> Int -> IO ()
leesRijen 0 a = return ()
leesRijen n a = do
   i <- read `liftM` getLine :: IO Int
   leesRij a i []
   leesRijen (n-1) (a+1)

leesRij :: Int -> Int -> [Int] -> IO ()
leesRij a 0 k = do
  print $ (show a)++" "++show(minimum k)++" "++show(maximum k)
leesRij a i k = do
  n <- read `liftM` getLine :: IO Int
  leesRij a (i-1) (n:k)

main = do
  n <- read `liftM` getLine :: IO Int
  leesRijen n 1
