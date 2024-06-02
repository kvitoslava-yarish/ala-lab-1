# Applied linear algebra
## Summary
### Talking about transformation matrices 2x2.
```
[a b]
[c d]
```
Element 𝑎: affects the scaling and rotation along the x-axis.

Element 𝑏, 𝑐:  contribute to the shearing effect. If ones are placed on b, c coordinates (x,y) -> (y,x)

Element 𝑑: affects the scaling and rotation along the y-axis.
### CV2 vs custom transformation functions
One key aspect of using cv2 for transformations is the requirement for the input matrix shape in the **cv2.transform** function. Specifically, cv2.transform expects the input matrix to be in the shape (1, a, b). So, this is because of frequently reshaping the input matrix to meet this requirement.
#### Shearing
Custom shearing and shearing in cv2 require different matrices to produce the same result
**Custom**
```
 def shear(self, axis:str, angle:float):
        angle = np.radians(angle)
        matrix = np.eye(2)
        if axis == 'x':
            matrix[1][0] = np.tan(angle)
        elif axis == 'y':
            matrix[0][1] = np.tan(angle)
        else:
            raise ValueError("incorrect axis")
        new_coordinates = self.coordinates @ matrix
        self.print_object(new_coordinates, "shear")
        return new_coordinates
```
**CV2**
```
def shear(self, axis:str, angle:float):
        angle = np.radians(angle)
        shear_matrix = np.eye(3)
        if axis == 'x':
            shear_matrix[0][1] =  np.tan(angle)
        elif axis == 'y':
            shear_matrix[1][0] =  np.tan(angle)
        else:
            raise ValueError("incorrect axis")
        new_coordinates = cv2.transform(self.coordinates,shear_matrix)[0]
        self.print_object(new_coordinates, "shear")
        return new_coordinates
```

Other transformations have the same matrices in cv2 and in custom functions 
