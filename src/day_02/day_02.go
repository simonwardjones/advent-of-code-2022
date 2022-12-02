package main

import (
	"fmt"
	"os"
	"strings"
)

func loadData(day int, isSample bool) string {
	fileName := "data.txt"
	if isSample {
		fileName = "sample_data.txt"
	}
	data, _ := os.ReadFile(fmt.Sprintf("inputs/day_%02d/%s", day, fileName))
	fileString := string(data)
	// fmt.Print(fileString) // Un-comment to see file
	return fileString
}

func getPoints(opponentChoice string, myChoice string) int {
	points := 0
	if opponentChoice == "A" && myChoice == "X" {
		points = 3 + 1 // rock rock
	} else if opponentChoice == "A" && myChoice == "Y" {
		points = 6 + 2 // rock paper
	} else if opponentChoice == "A" && myChoice == "Z" {
		points = 0 + 3 // rock scissors
	} else if opponentChoice == "B" && myChoice == "X" {
		points = 0 + 1 // paper rock
	} else if opponentChoice == "B" && myChoice == "Y" {
		points = 3 + 2 // paper paper
	} else if opponentChoice == "B" && myChoice == "Z" {
		points = 6 + 3 // paper scissors
	} else if opponentChoice == "C" && myChoice == "X" {
		points = 6 + 1 // scissors rock
	} else if opponentChoice == "C" && myChoice == "Y" {
		points = 0 + 2 // scissors paper
	} else if opponentChoice == "C" && myChoice == "Z" {
		points = 3 + 3 // scissors scissors
	}
	return points
}

func partOne() {
	fmt.Println("Running part 1.")
	data := loadData(2, false)
	totalPoints := 0
	for _, round := range strings.Split(data, "\n") {
		round := strings.Fields(round)
		opponentChoice := round[0]
		myChoice := round[1]
		points := getPoints(opponentChoice, myChoice)
		// fmt.Println(opponentChoice, myChoice, points)
		totalPoints += points
	}
	fmt.Println(totalPoints)
}

func getPointsFromDecision(opponentChoice string, myChoice string) int {
	points := 0
	if opponentChoice == "A" && myChoice == "X" {
		points = 0 + 3 // rock lose
	} else if opponentChoice == "A" && myChoice == "Y" {
		points = 3 + 1 // rock draw
	} else if opponentChoice == "A" && myChoice == "Z" {
		points = 6 + 2 // rock win
	} else if opponentChoice == "B" && myChoice == "X" {
		points = 0 + 1 // paper lose
	} else if opponentChoice == "B" && myChoice == "Y" {
		points = 3 + 2 // paper draw
	} else if opponentChoice == "B" && myChoice == "Z" {
		points = 6 + 3 // paper win
	} else if opponentChoice == "C" && myChoice == "X" {
		points = 0 + 2 // scissors lose
	} else if opponentChoice == "C" && myChoice == "Y" {
		points = 3 + 3 // scissors draw
	} else if opponentChoice == "C" && myChoice == "Z" {
		points = 6 + 1 // scissors win
	}
	return points
}

func partTwo() {
	fmt.Println("Running part 2.")
	data := loadData(2, false)
	totalPoints := 0
	for _, round := range strings.Split(data, "\n") {
		round := strings.Fields(round)
		opponentChoice := round[0]
		myChoice := round[1]
		points := getPointsFromDecision(opponentChoice, myChoice)
		// fmt.Println(opponentChoice, myChoice, points)
		totalPoints += points
	}
	fmt.Println(totalPoints)
}

func main() {
	fmt.Println("Running day 1.")
	partOne()
	partTwo()
	fmt.Println("Finished day 1.")
}
