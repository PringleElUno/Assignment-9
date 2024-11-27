# Author: Luis Pringle
# GitHub username: PringleElUno
# Date: 11/26/2024
# Define a Point class that has two data members, _x_ coord and _y_coord, representing the two
# coordinates of the point

# Defining the point class and initializing it
class Point:
    def __init__(self, x_coordinate, y_coordinate):
        """
       Initializes the point object with the x and y coordinates.
    
        Parameters:
            x_coordinate (float): The x_coordinate of the point.
            y_coordinate (float): The y_coordinate of the point.
         """
        self._x_coordinate = x_coordinate
        self._y_coordinate = y_coordinate

# Setting up the getter methods
    def get_x_coordinate(self):
        """
        Gets the x_coordinate of the point.

        Returns:
            float: The x_coordinate.
        """
        return self._x_coordinate

    def get_y_coordinate(self):
        """
        Gets the y_coordinate of the point.

        Returns:
            float: The y_coordinate.
        """
        return self._y_coordinate

    #The __init__, get_x_coordinate, and get_y_coordinate are defined
    def distance_to(self, other_point):
        """
        Calculate the distance between the Point object and the other Point object.

        Parameters:
            other_point (Point): The distance calculated with the point object.

        Returns:
            float: Between the distance of two points.
        """

        # Calculate the distance directly from the given formula
        x_diff = self._x_coordinate - other_point.get_x_coordinate()
        y_diff = self._y_coordinate - other_point.get_y_coordinate()
        return (x_diff ** 2 + y_diff ** 2) ** 0.5

# Creating the class LineSegment that has two of the data members endpoint_1 and endpoint_2
class LineSegment:
    def __init__(self, endpoint_1, endpoint_2):
        """
        Initialize the LineSegment object utilizing the two end points.

        Parameters:
            endpoint_1 (Point): The first endpoint of the LineSegment.
            endpoint_2 (Point): The second endpoint of the LineSegment.
        """

        self.endpoint_1 = endpoint_1
        self.endpoint_2 = endpoint_2

# Setting up the getter methods for each end point
    def get_endpoint_1(self):
        """
        Gets the first end point of the LineSegment.

        Return:
             Point: The first end point.
        """
        return self.endpoint_1

    def get_endpoint_2(self):
        """
        Gets the second end point of the LineSegment.

        Returns:
            Point: The second end point.
        """
        return self.endpoint_2

# Defining the length of the LineSegments between the end points
    def length(self):
        """
        Calculate the length of the LineSegment utilizing the distance between both end points.

        Returns:
            Float: The length of the LineSegment.
        """
        x_diff = self.endpoint_1.get_x_coordinate() - self.endpoint_2.get_x_coordinate()
        y_diff = self.endpoint_1.get_y_coordinate() - self.endpoint_2.get_y_coordinate()
        return (x_diff ** 2 + y_diff ** 2) ** 0.5

# Defining the slope between the end points
    def slope(self):
        """
        Calculates the slope of the LineSegment.

        Returns:
            float: The slope of the LineSegment.
        """

        x_coordinate_of_endpoint1 = self.endpoint_1.get_x_coordinate()
        x_coordinate_of_endpoint2 = self.endpoint_2.get_x_coordinate()
        y_coordinate_of_endpoint1 = self.endpoint_1.get_y_coordinate()
        y_coordinate_of_endpoint2 = self.endpoint_2.get_y_coordinate()

        if x_coordinate_of_endpoint1 == x_coordinate_of_endpoint2:
            return None

        return (y_coordinate_of_endpoint2 - y_coordinate_of_endpoint1) / (x_coordinate_of_endpoint2 - x_coordinate_of_endpoint1)

# Defined the method is_parallel_to find if the LineSegment is parallel to the other
    def is_parallel_to(self, line_segment2):
        """
        Checks if the current LineSegment is parallel to the other LineSegment.

        Parameters:
            line_segment2 (LineSegment): The second LineSegment to compare with.


        Returns:
            bool: True if the Line segments are parallel, false if they are not parallel.
        """

        slope_of_first_line = self.slope()
        slope_of_second_line = line_segment2.slope()

        if slope_of_first_line is None or slope_of_second_line is None:
            return slope_of_first_line == slope_of_second_line

        return abs(slope_of_first_line - slope_of_second_line) < 0.000001
