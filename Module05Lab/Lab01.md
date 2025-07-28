## Lab01 Classes

### Triangle class

1. Create a class to represent a triangle.  Store just the three sides of the triangle.  DON'T attempt to store angles as well

    Your constructor should check for an invalid triangle:
    - negative side length
    - any pair of sides adding up to less than the length of the third side
    - the right thing to do for an invalid triangle would be to throw an exception.  If you don't know how to do that then just print a message

1. Add a member function `get_perimeter(self)` to calculate the perimeter of the triangle.

1. Write some test code to show that you can create triangles and compute their perimeters

1. Print out the detail of a triangle, (all three sides and perimeter).  Don't add a member function for this, write lines like:
    - print(triangle1.side1)
    - print(triangle1.get_perimeter())

1. Notice this is inconsistent syntax. To retrieve the perimeter requires very different syntax (`get_perimeter(self)`)

1. Add a property definition for perimeter to the class
    `perimeter = property(get_perimeter)`
(notice that you MUST NOT have parentheses (like `()`) after get_perimeter)
1. Now find that you can access the attribute `perimeter` of the class *as if* it were simple read only data.  The property automates calling the `get_perimeter` function, and returning its result

### Bonus Ideas

1. Add a colour attribute, as a string, to the Triangle class.  In the constructor default it to "Black"
1. Print the triangle colour as well as the side lengths
1. Notice that you can set the colour to any random value by simple assignment
    `t1.colour = "Dog"`
    obviously dog is not a valid colour value

#### Make colour a property
1. Change the name `colour` to `_colour` thoughout the class.  It is a python convention that leading underscore vaeibles are considered `private` and programmers using the class should NOT touch them.  It is just a convention the language does not enforce it.
Add a `get_colour(self)` function and a `set_colour(self, newColour)` function to your class
Add a property for `colour` like this...
    `colour = property(get_colour, set_colour)`
Retest your code.  Discover that you can still set `colour` (NOT `_colour` you should not touch that) to silly values
1. In the `set_colour` function add protection code so that it will ONLY accept the colour values "Red", "Blue" "Green".  Again the right thing to do for an invalid value would be to throw an exception.  If you don't know how to do that just print a message.
1. Discover that assignments to `colour` are now validated by the logic in `set_colour`