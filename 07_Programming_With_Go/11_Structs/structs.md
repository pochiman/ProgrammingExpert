# Key Term

# [Struct]
In Go, a `struct` is a typed collection of fields that can be treated like a custom 
type (like a class in Python). Structs are useful for grouping data together, they 
can contain fields and methods.

`type Person struct {`
    `firstName string`
    `lastName  string`
    `age       int`
`}`

`func (p Person) getName() string {`
    `return p.firstName + " " + p.lastName`
`}`