# Key Term

# [Go_Interface]
In Go, an `interface` is a typed collection of method signatures that can be treated 
like a custom type. Interfaces define a set of methods that any struct that implements 
the interface must implement.

`type Pricing interface {`
    `getDiscount() float64`
    `getTax()      float64`
`}`