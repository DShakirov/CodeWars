package main

import (
	"fmt"
	"math"
)

func NbMonths(startPriceOld, startPriceNew, savingperMonth int, percentLossByMonth float64) [2]int {
	saving := float64(0)
	priceOfOldCar := float64(startPriceOld)
	priceOfNewCar := float64(startPriceNew)
	if priceOfNewCar <= priceOfOldCar {
		return [2]int{0, int(priceOfOldCar - priceOfNewCar)}
	}
	months := 0
	for {
		months += 1
		if months > 1 && months%2 == 0 {
			percentLossByMonth += 0.5
		}
		saving += float64(savingperMonth)
		priceOfNewCar -= priceOfNewCar * (percentLossByMonth / 100)
		priceOfOldCar -= priceOfOldCar * (percentLossByMonth / 100)
		if priceOfOldCar+saving >= priceOfNewCar {
			charge := math.Round(priceOfOldCar + saving - priceOfNewCar)
			return [2]int{months, int(charge)}
		}
	}
}

func main() {
	fmt.Println(NbMonths(2000, 8000, 1000, 1.5))
}
