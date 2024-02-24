package main

import (
	"fmt"
)

func Multiple3And5(number int) int {
	r := 0
	for i := 2; i < number; i++ {
		if i%3 == 0 || i%5 == 0 {
			r += i
		}
	}
	return r
}

func main() {
	fmt.Println(Multiple3And5(10))
}
