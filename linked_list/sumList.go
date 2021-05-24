package main

import (
	"fmt"
)


type Node struct {

	data int
	next *Node

}


func doPadding(head *Node, padding int){

	for i:=0; i< padding; i++ {
	
		newNode := Node{data:0}
		newNode.next = head.next
		head.next = &newNode
	}
	
}


func makeEqualSize(head1 *Node, head2 *Node) {


	var size1, size2 int
	
	var current *Node
	
	
	current = head1
	for current.next != nil {
		size1++
		current = current.next
	}
	
	current = head2
	for current.next != nil {
		size2++
		current = current.next
	}
	
	
	if size1 > size2 {
	
		doPadding(head2, size1-size2)
		
	} else if size1 < size2 {
	
		doPadding(head1, size2-size1)
	}
	

}


func findSumRec(head1 *Node, head2 *Node, result *Node) int {


	if head1 == nil && head2 == nil {
		return 0
	}
	
	resultNode := &Node{}
	result.next = resultNode
	
	var next1, next2 *Node
	var data1, data2 int
	
	if head1 != nil {
		next1 = head1.next
		data1 = head1.data
	}
	
	if head2 != nil {
		next2 = head2.next
		data2 = head2.data
	}
	
	carry := findSumRec(next1, next2, resultNode)
	
	sum := data1 + data2 + carry
	
	resultNode.data = sum % 10
	
	return sum/10

}

func printList(head *Node) {

	for head != nil {
		fmt.Print(head.data)
		head = head.next
	}
}


func findSum(head1 *Node, head2 *Node) *Node {

	makeEqualSize(head1, head2)

	resultNode := &Node{}
	
	finalCarry := findSumRec(head1, head2, resultNode)
	
	if finalCarry == 1 {
	
		resultNode.data = 1
		return resultNode
	} 
	
	return resultNode.next

}


func main() {

	firstNum := []int{7,8,9,9}
	secondNum := []int{5,6,7}
	
	firstHead := &Node{}
	secondHead := &Node{}
	
	var currentHead *Node
	
	currentHead = firstHead
	for _, val := range firstNum {
	
		newNode := Node{data: val}
		currentHead.next = &newNode
		currentHead = &newNode
	}
	
	currentHead = secondHead
	for _, val := range secondNum {
	
		newNode := Node{data: val}
		currentHead.next = &newNode
		currentHead = &newNode
	}
	
	resultHead := findSum(firstHead, secondHead)
	
	printList(resultHead)
}

