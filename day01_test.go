package main

import "testing"

func Test_day01(t *testing.T) {
	type args struct {
		lines []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			"from website",
			args{[]int{199, 200, 208, 210, 200, 207, 240, 269, 260, 263}},
			5,
		},
		{
			"two elements",
			args{[]int{199, 200}},
			0,
		},
		{
			"empty",
			args{[]int{}},
			0,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := day01(tt.args.lines); got != tt.want {
				t.Errorf("day01() = %v, want %v", got, tt.want)
			}
		})
	}
}
