package main

import (
	"fmt"
)

func main() {
	fmt.Println("gimmie yo length so i can be done with this project")
  var len int
  fmt.Scanln(&len)

  fmt.Println("alr now the width and we're done")
  var wid int
  fmt.Scanln(&wid)

  var area int = len * wid
  var perim int = ((len * 2) + (wid * 2))

  fmt.Println("\n\nlord please let this work first try\n\n")

  fmt.Println("your area is: ", area)
  fmt.Println("your perimeter is: ", perim)
  
}
