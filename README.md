# Session 10 Readme file 
# Assignment details:

# Problem #1
   Create a Polygon Class:
        where initializer takes in:
              o  number of edges/vertices
              o  circumradius
        that can provide these properties:
              o edges
              o vertices
              o interior angle
              o edge length
              o apothem
              o area
              o perimeter
        that has these functionalities:
              o a proper __repr__ function
              o implements equality (==) based on # vertices and circumradius (__eq__)
              o implements > based on number of vertices only (__gt__)
# Solution 1
    * The Polygon Class is intialized  with the following parameters (computed as per formulae given below)
                int_angle = (s-2) * 180.0/s  --> Interior angle
                edge_len = 2 * r * math.sin(math.pi/s)  --> length of one edge
                apothem = r * math.cos(math.pi/s)   --> distance between the center and line joining two vertices
                area = 0.5 * s * self.edge_len * self.apothem  --> area of the polygon
                perimeter = s * edge_len  --> Perimeter
                vertices = No. of vertices = no. of edges --> No of vertices
        + self.edges = s                              # --> No. of edges
        + self.radius = r                             # --> Circum radius
        + self.int_angle = (s - 2) * 180.0 / s        # --> Interior angle
        + self.edge_len = 2 * r * math.sin(math.pi / s)  # --> Edge length
        + self.apothem = r * math.cos(math.pi / s)       # --> apothem 
        + self.area = 0.5 * s * self.edge_len * self.apothem  # --> area of polygon
        + self.perimeter = s * self.edge_len             # --> perimeter of polygon
        + self.vertices = s                              # No.of vertices in the polygon

    The __repr__() function prints the following information
        * Regular polygon with {self.edges} sides and circum radius = {self.radius}')
        The class object with the following parameters initialized')
            + edges     --> No. of edges = {self.edges}
            + radius    --> circum radius = {self.radius}
            + int_angle --> Interior angle = {self.int_angle}
            + edge_len  --> length of one edge = {self.edge_len}
            + apothem   --> distance between the center and line joining two verticesi = {self.apothem}
            + area      --> area of the polygon = {self.area}
            + perimeter --> perimeter  = {self.perimeter}
            + vertices  --> No of vertices = {self.vertices}
    
# Problem 2
    Implement a Custom Polygon sequence type:
        where initializer takes in:
            * number of vertices for largest polygon in the sequence
            * common circumradius for all polygons
        that can provide these properties:
            * max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
        that has these functionalities:
            * functions as a sequence type (__getitem__)
            * supports the len() function (__len__)
            * has a proper representation (__repr__)
# Solution 2
   * The PolygonSeq class object initialized as follows
        self.n = n  # Maximum no. of polygon available in the sequence
        self.r = r
        self.max_eff_n = 3
        self.max_eff = 0
        self.curr_poly = n  # default polygon index
     and the maximum efficiency polygon is computed as follows
        max_eff = 0
        for i in range(3, n + 1):
            temp_poly = self._polygon(i, r)
            eff = temp_poly.area / temp_poly.perimeter
            if self.max_eff < eff:
                self.max_eff = eff
                self.max_eff_n = i
    where the getitem for each entry in the sequence is computed and cached used lru_cache
    @staticmethod
    @lru_cache(maxsize=100)
    def _polygon(s, r):
        """
        Computes the polygon of given order and radius
        Args:
            s: Polygon order
            r: Circum radius of the polygon
        Returns:
            The polygon class object
        """
        return Polygon(s, r)

    * The __repr__() function displays the following
        + Polygon sequence of length = {self.n} with radius = {self.r}
        + The maximum efficiency polygon is with edges = {self.max_eff_n}
        + The maximum efficiency (area/perimeter) is {self.max_eff}

# Test cases

   * The following test cases are added:
   
     o Test case 1: Checks invalid poygon order
     
     o Test case 2: Checks the valid edges in the class object
     
     o Test case 3: Checks the area computation
     
     o Test case 4: Checks the equality of two polygon objects
     
     o Test case 5: Checks the greater than function for Polygon objects
     
     o Test case 6: Checks the length function
     
     o Test case 7: Checks the Polygon Sequence creation
     
     o Test case 8: Checks the _next polygon in the sequence function
     
     o Test case 9: Checks the _prev polygon in the sequence function
     
     o Test case 10: Checks the custom sequence creation 
      
# A readme file 
    * (this file) describes the code and solution approach and the test cases. 

# A py notebook 
    * which tests the above are given for verification in colab. 

# End of file
 