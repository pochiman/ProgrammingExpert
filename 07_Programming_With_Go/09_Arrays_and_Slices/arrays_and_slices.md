# Key Terms

# [Array]
In Go, an `array` is a fixed size data structure that stores elements of a single type. 
The size of an array is part of its type and once an array is created, its size cannot 
change.

`myArray := [5]int{1, 2, 3, 4, 5}`  // an integer array of size 5

# [Slice]
In Go, a `slice` is a dynamically sized, view of the elements of an underlying array. 
Every slice has a length, capacity, and pointer to an underlying array. Modifying a 
slice will modify the elements of the underlying array it references. Slices are more 
flexible than arrays and are commonly used in place of them in Go.

`mySlice := []int{1, 2, 3, 4, 5}`  // an integer slice of length 5