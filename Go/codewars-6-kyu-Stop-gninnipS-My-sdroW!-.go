package main

import (
	"fmt"
	"strings"
)

func SpinWords(str string) string {
	s := ""
	arr := strings.Fields(str)
	for _, word := range arr {
		if len(word) > 4 {
			reversed := Reverse(word)
			s += reversed + " "
		} else {
			s += word + " "
		}

	}
	return strings.TrimSpace(s)
}

func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func main() {
	fmt.Println(SpinWords("Hey fellow warriors"))
}
