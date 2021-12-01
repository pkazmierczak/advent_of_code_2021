package main

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
