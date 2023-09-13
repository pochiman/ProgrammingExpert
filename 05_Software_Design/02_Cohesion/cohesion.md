# Key Term

# [Cohesion]
`Cohesion` refers to the degree to which things grouped together are similar. Usually, when 
programming, you would like to increase cohesion. There are many different types of cohesion:

 • `Functional`: facilities are kept together that perform only one computation with no side effects.
 • `Layer`: related services are kept together.
 • `Communicational`: facilities for operating on the same data are kept together.
 • `Sequential`: a set of procedures, which work in sequence to perform some computation are kept together.
 • `Procedural`: a set of procedures, which are called one after another are kept together. 
 • `Temporal`: procedures used in the same general phase of execution like initialization and cleanup are kept together.
 • `Utility`: related utilities are kept together (when there is no way to group using strong cohesion).