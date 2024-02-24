package main

import (
	"fmt"
)

func FindOdd(seq []int) int {
	m := make(map[int]int)
	for _, n := range seq {
		if _, ok := m[n]; !ok {
			m[n] = 1
		} else {
			m[n]++
		}
	}
	for key, value := range m {
		if value == 1 || value%2 != 0 {
			return key
		}
	}
	return 0
}

func main() {
	fmt.Println(FindOdd([]int{1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1}))
}
