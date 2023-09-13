# Key Term

# [Pointer]
In Go, a `pointer` is a data type that stores the memory address location of a value. 
Pointers are represented with an asterisk (*) before the type of the value that they 
point to (e.g. `*int` is a pointer to an integer). To get a pointer to a value, you 
use the `&` operator, and to reference a pointer, you use the `*` operator.

`num := 1`
`var numPointer *int = &num`
`*numPointer = 2`
// num is now equal to 2