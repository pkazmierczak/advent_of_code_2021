package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func readLines(path string) []int {
	file, _ := os.Open(path)
	defer file.Close()

	var lines []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		num, _ := strconv.Atoi(scanner.Text())
		lines = append(lines, num)
	}
	return lines
}

func main() {
	fmt.Println(day01(readLines("day01.txt")))
}
