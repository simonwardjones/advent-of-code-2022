package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func loadData(day int, isSample bool) string {
	fileName := "data.txt"
	if isSample {
		fileName = "sample_data.txt"
	}
	data, err := os.ReadFile(fmt.Sprintf("inputs/day_%02d/%s", day, fileName))
	check(err)
	fileString := string(data)
	// fmt.Print(fileString) // Un-comment to see file
	return fileString
}

func main() {
	fmt.Println("Running day 1.")
	partOne()
	partTwo()
	fmt.Println("Finished day 1.")
}

func partOne() {
	fmt.Println("Running part 1.")
	data := loadData(1, false)
	elfStrings := strings.Split(data, "\n\n")
	var elfTotals []int
	var maxElfCalories int = 0
	for _, elfString := range elfStrings {
		elfList := strings.Split(elfString, "\n")
		var elfTotal int
		for _, calories := range elfList {
			calories, _ := strconv.Atoi(calories)
			elfTotal += calories
		}
		elfTotals = append(elfTotals, elfTotal)
		if elfTotal > maxElfCalories {
			maxElfCalories = elfTotal
		}
	}
	// fmt.Println(elfTotals)
	fmt.Println(maxElfCalories)
}

func partTwo() {
	fmt.Println("Running part 2.")
	data := loadData(1, false)
	elfStrings := strings.Split(data, "\n\n")
	var elfTotals []int
	for _, elfString := range elfStrings {
		elfList := strings.Split(elfString, "\n")
		var elfTotal int
		for _, calories := range elfList {
			calories, _ := strconv.Atoi(calories)
			elfTotal += calories
		}
		elfTotals = append(elfTotals, elfTotal)
	}

	sort.Sort(sort.Reverse(sort.IntSlice(elfTotals)))
	total := 0
	for i := 0; i < 3; i++ {
		total += elfTotals[i]
	}
	// fmt.Println(elfTotals)
	fmt.Println(total)
}
