package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func day01(lines []int) int {
	increase, last := 0, 0

	for idx := 0; idx < len(lines)-2; idx++ {
		num1 := lines[idx]
		num2 := lines[(idx+1)%len(lines)]
		num3 := lines[(idx+2)%len(lines)]
		sum := num1 + num2 + num3
		if last != 0 {
			if sum > last {
				increase++
			}
		}
		last = sum
	}
	return increase
}

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
	fmt.Println(day01(readLines("../day01.txt")))
}
