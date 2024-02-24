package main

import (
	"fmt"
	"strconv"
	"strings"
)

func StockList(listArt []string, listCat []string) string {
	if len(listArt) == 0 || len(listCat) == 0 {
		return ""
	}
	d := make(map[string]int)
	for _, i := range listCat {
		d[i] = 0
	}
	for _, art := range listArt {
		y := string(art[0])
		if _, ok := d[y]; ok {
			x := strings.Split(art, " ")[1]
			xint, err := strconv.Atoi(x)
			if err != nil {
				return ""
			}
			d[y] += xint

		}
	}
	fmt.Println(d)
	r := string("")
	for _, i := range listCat {
		r += fmt.Sprintf("(%s : %s) - ", i, strconv.Itoa(d[i]))
	}
	trimmedR := strings.TrimSuffix(r, r[len(r)-3:])
	return trimmedR
}

func main() {
	fmt.Println(StockList([]string{"BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"}, []string{"A", "B", "C", "D"}))
}
