//PF-Exer-24
//This verification is based on string match.

package main

import ("fmt")
func main() {
    //Write your program logic here
    var number int=3
    fmt.Println(find_square(number))
}
func find_square(number int) int{
    var square int=number*number
    return square
}
