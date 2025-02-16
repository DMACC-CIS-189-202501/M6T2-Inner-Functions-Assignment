# TODO 1: Enter your DocString here

def measurements(a_list):
    def area(a_list):
        # TODO 4: Calculate the area and return it
        # Hint: You can use len(), so if len(a_list) is 1 it is a square and if it is 2 it is a rectangle
        # after you have your calculation and return statement delete the 'pass'

        pass
    def perimeter(a_list):
        # TODO 5: Calculate the perimeter and return it
        # Hint: You can use len(), so if len(a_list) is 1 it is a square and if it is 2 it is a rectangle
        # after you have your calculation and return statement delete the 'pass'

        pass
    
    #measurements runner code
    the_area = area(a_list) # Notice this calls the inner function area
    the_perimeter = perimeter(a_list) #notice this calls the inner funciton perimeter

    # TODO 2: Add a return statement to return a string in the format
    # "Perimeter = {the_perimeter} Area = {the_area}"
    # Remember to round to 2 decimal places


    #Todo 3: Delete this pass when your return statement is done and this comment
    pass

if __name__ == '__main__':
    rectangle = [2.1, 3.4]
    result = measurements(rectangle)
    print(result) #Expected to be "Perimeter = 11.00 Area = 7.14"
    square = [3.5]
    result = measurements(square)
    print(result) #Expected to be "Perimeter = 14.00 Area = 12.25"
    #Note: Try to uncomment these, notice they show an error as area and perimeter are inner funcitons so they cannot be referenced; then re-comment them so the autograder can work.
    #area([3.5])
    #perimeter([3.5])