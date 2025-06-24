## Lab02 Inheritance

### Shape class

1. Continue working in the same file as where your Triangle class is

1. Create a class Shape

1. Have it store a position (Just pass and store an x co-ordinate and a y co-ordinate in the constructor)

1. Now make Triangle inherit from Shape.  It looks like this
    `class Triangle(Shape)`
    ...this means that Triangle should have all the attributes of Shape...

1. To enforce that, when we create a `Triangle` we should add an x and a y coordinate.  So extend `Triangle.__init__` to accept an x and a y parameter.
1. Pass those values up to the `Shape` class constructor using the built in `super()` function.  Like this...
    `super().__init__(x, y)`
    notice that this automatically passes the `self` object
1. Retest your code.  Notice that creating a `Triangle` now requires an x and y co-ordinate


### Bonus ideas...

### Demonstrate polymorphism

1. Create a `Square` class that also inherits from `Shape`.  Have square store a width and a height
1. Don't forget that the `Square` constructor should have an x and a y co-ordinate parameters.  It should also pass them up to `Square` using the `super()` function (just like `Triangle`)
1. Give `Square` a read only `perimiter` property
1. Test this by creating a list with a `Triangle` and a `Square`.  Iterate over the list and access the `perimiter` property for both objects.  Your code might look like this (A hint in case you don't know how to create a list and iterate over it)...
```
shapes = [ Triangle(2,2,3, 100, 110), Square(10,10, 110, 120) ]
for shape in shapes:
    print(shape.perimiter)

```



