# M6 T2: Inner Functions Assignment

TODO: Update the above to your repo name

## Instructions for students

- Implement your solutions in `assignment.py`
- The tests in `test_assignment.py` can be inspected but do not modify them

### Directions - Copy/Pasted from Canvas

TODO

### Example Input and Output

* define a function called  ```measurements``` that takes in a shape, defined by a list of lengths
* if length of sides is 1, it is a square
* if length of sides is 2, it is a rectangle
  * define an inner function called ```area(a_list)```
    * this should calculate the area of the shape and return it
    * area is length times width
  * define an inner function called ```perimeter(a_list)```
    * this should calculate the perimeter and return it
    * perimeter is side1 + side2 + side3 + side4; or 2*side1 + 2*side2
    * note that in a square, all sides are equal, and in a rectangle side1 and 3 are equal and sides 2 and 4 are equal

Calling the function may look like:
~~~python
if __name__ == '__main__':
    rectangle = [2.1, 3.4]
    result = measurements(rectangle)
    print(result)
    square = [3.5]
    result = measurements(square)
    print(result)
~~~

| Input | Expected Output | Note |
| ---- | ---- | ---- |
| rectangle = [2.1, 3.4]<br/>result = measurements(rectangle) | ```Perimeter = 11.00 Area = 7.14``` | Round to 2 decimal places using .2f string formatting |
| square = [3.5]<br/>result = measurements(square) | ```Perimeter = 14.00 Area = 12.25``` | Round to 2 decimal places using .2f string formatting |
