"""Hops flask middleware example"""
from flask import Flask
import ghhops_server as hs
import rhino3dm


# register hops app as middleware
app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)


# flask app can be used for other stuff drectly
@app.route("/help")
def help():
    return "Welcome to Grashopper Hops for CPython!"



@hops.component(
    "/binmult",
    inputs=[
        hs.HopsNumber("A"), 
        hs.HopsNumber("B")
        ],
    outputs=[
        hs.HopsNumber("Multiply")
        ],
)
def BinaryMultiply(a: float, b: float):
    return a * b

@hops.component(
    "/add",
    name="Add",
    nickname="Add",
    description="Add numbers with CPython",
    inputs=[
        hs.HopsNumber("A", "A", "First number"),
        hs.HopsNumber("B", "B", "Second number"),
    ],
    outputs=[hs.HopsNumber("Sum", "S", "A + B")]
)
def add(a: float, b: float):
    return a + b

#write a subtract component here in @hops format
@hops.component(
    "/subtract",
    name="Subtract",
    nickname="Sub",
    description="Subtract numbers with CPython",
    inputs=[
        hs.HopsNumber("A", "A", "First number"),
        hs.HopsNumber("B", "B", "Second number"),
    ],
    outputs=[hs.HopsNumber("Difference", "D", "A - B")]
)
def subtract(a: float, b: float):
    return a - b


@hops.component(
    "/pointat",
    name="PointAt",
    nickname="PtAt",
    description="Get point along curve",
    icon="pointat.png",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameter on Curve to evaluate")
    ],
    outputs=[hs.HopsPoint("P", "P", "Point on curve at t")]
)
def pointat(curve: rhino3dm.Curve, t=0.0):
    return curve.PointAt(t)


@hops.component(
    "/srf4pt",
    name="4Point Surface",
    nickname="Srf4Pt",
    description="Create ruled surface from four points",
    inputs=[
        hs.HopsPoint("Corner A", "A", "First corner"),
        hs.HopsPoint("Corner B", "B", "Second corner"),
        hs.HopsPoint("Corner C", "C", "Third corner"),
        hs.HopsPoint("Corner D", "D", "Fourth corner")
    ],
    outputs=[hs.HopsSurface("Surface", "S", "Resulting surface")]
)
def ruled_surface(a: rhino3dm.Point3d,
                b: rhino3dm.Point3d,
                c: rhino3dm.Point3d,
                d: rhino3dm.Point3d):
    edge1 = rhino3dm.LineCurve(a, b)
    edge2 = rhino3dm.LineCurve(c, d)
    return rhino3dm.NurbsSurface.CreateRuledSurface(edge1, edge2)

"""
██████╗ ██╗  ██╗██╗   ██╗███████╗██╗ ██████╗███████╗
██╔══██╗██║  ██║╚██╗ ██╔╝██╔════╝██║██╔════╝██╔════╝
██████╔╝███████║ ╚████╔╝ ███████╗██║██║     ███████╗
██╔═══╝ ██╔══██║  ╚██╔╝  ╚════██║██║██║     ╚════██║
██║     ██║  ██║   ██║   ███████║██║╚██████╗███████║
╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝ ╚═════╝╚══════╝
"""
#A Scalar Quantity is a quantity that can be described by a single number
#a scalar has nothing to do with vectors or direction
#such as length, mass, volume, speed, temperature, density, pressure, energy, work, power, etc. 
#example 
#   1. 5 meters
#   2. 10 kilograms
#   3. 20 degrees Celsius

#Distance (l) is a scalar quantity that refers to "how much ground an object has covered" during its motion.
#path length
#(l) is used because (d) is used for derivatives

#Average Speed(v) is a scalar quantity that refers to "how fast an object is moving."
#equation for average speed is v = d/t
#example
l = 5 #meters
t = 2 #seconds
v = l/t #meters per second
print(v)

#write into @hops format
@hops.component(
    "/average_speed",
    name="Average Speed",
    nickname="AvgSpd",
    description="Calculate average speed",
    inputs=[
        hs.HopsNumber("Distance", "D", "Distance traveled"),
        hs.HopsNumber("Time", "T", "Time taken"),
    ],
    outputs=[hs.HopsNumber("Speed", "S", "Average speed")]
)
def average_speed(d: float, t: float):
    return d / t

#constant speed is when the speed of an object is the same at all times
#distance vs time graph for constant speed is a straight line
#average speed = instantaneous speed

#Instantaneous Speed is a scalar quantity that refers to "how fast an object is moving" at a particular moment. 
#equation is v = lim (t->0) (d/t) or v = d/t
#this introduces the concept of a limit, calculus, and derivatives
#example of instantaneous speed in an equation
v = 3*t**2 + 2*t + 1
print(v)

#write into @hops format
@hops.component(
    "/instantaneous_speed",
    name="Instantaneous Speed",
    nickname="InstSpd",
    description="Calculate instantaneous speed",
    inputs=[
        hs.HopsNumber("Time", "T", "Time taken"),
    ],
    outputs=[hs.HopsNumber("Speed", "S", "Instantaneous speed")]
)
def instantaneous_speed(t: float):
    return 3*t**2 + 2*t + 1

#A Vector Quantity is a quantity that has both magnitude and direction
#such as displacement, velocity, acceleration, force, momentum, etc.
#example
#   1. 5 meters north
#   2. 10 kilograms north
#   3. 20 degrees Celsius north
#represented with bold face letters or with an arrow above the symbol
#example
#   1. v = 5 m/s north
#   2. F = 10 N north
#   3. a = 20 m/s^2 north

#Displacement (d) is a vector quantity that refers to "how far out of place an object is"; it is the object's overall change in position.
#equation for displacement is d = xf - xi
#example
xi = 5 #meters
xf = 10 #meters
d = xf - xi #meters
print(d)

#write into @hops format
@hops.component(
    "/displacement",
    name="Displacement",
    nickname="Disp",
    description="Calculate displacement",
    inputs=[
        hs.HopsNumber("Initial Position", "Xi", "Initial position"),
        hs.HopsNumber("Final Position", "Xf", "Final position"),
    ],
    outputs=[hs.HopsNumber("Displacement", "D", "Displacement")]
)
def displacement(xi: float, xf: float):
    return xf - xi

#create an example of a vector quantity from 2 3D points in the @hops format
@hops.component(
    "/vector",
    name="Vector",
    nickname="Vec",
    description="Create vector from two points",
    inputs=[
        hs.HopsPoint("Point A", "A", "First point"),
        hs.HopsPoint("Point B", "B", "Second point"),
    ],
    outputs=[hs.HopsVector("Vector", "V", "Resulting vector")]
)
def vector(a: rhino3dm.Point3d, b: rhino3dm.Point3d):
    return rhino3dm.Vector3d(b.X - a.X, b.Y - a.Y, b.Z - a.Z)

#Velocity (v) is a vector quantity that refers to "the rate at which an object changes its position."
#equation for velocity is v = d/t
#equartion for average velocity is v = (xf - xi)/(tf - ti)
#example
xi = 5 #meters
xf = 10 #meters
ti = 0 #seconds
tf = 2 #seconds
v = (xf - xi)/(tf - ti) #meters per second
print(v)

#write into @hops format
@hops.component(
    "/average_velocity",
    name="Average Velocity",
    nickname="AvgVel",
    description="Calculate average velocity",
    inputs=[
        hs.HopsNumber("Initial Position", "Xi", "Initial position"),
        hs.HopsNumber("Final Position", "Xf", "Final position"),
        hs.HopsNumber("Initial Time", "Ti", "Initial time"),
        hs.HopsNumber("Final Time", "Tf", "Final time"),
    ],
    outputs=[hs.HopsNumber("Velocity", "V", "Average velocity")]
)
def average_velocity(xi: float, xf: float, ti: float, tf: float):
    return (xf - xi)/(tf - ti)

#instantaneous velocity is the velocity of an object in motion at a specific point in time
#equation for instantaneous velocity is v = lim (t->0) (d/t) or v = d/t
#this introduces the concept of a limit, calculus, and derivatives
#example of instantaneous velocity in an equation
v = 3*t**2 + 2*t + 1
print(v)

#write into @hops format
@hops.component(
    "/instantaneous_velocity",
    name="Instantaneous Velocity",
    nickname="InstVel",
    description="Calculate instantaneous velocity",
    inputs=[
        hs.HopsNumber("Time", "T", "Time taken"),
    ],
    outputs=[hs.HopsNumber("Velocity", "V", "Instantaneous velocity")]
)
def instantaneous_velocity(t: float):
    return 3*t**2 + 2*t + 1

#the addition of vectors is called vector addition
#the result of vector addition is called the resultant
#the resultant is the sum of two or more vectors
#find the resultant of two vectors by placing the tail of the second vector at the head of the first vector 
#from three points, create two vectors and add them together
@hops.component(
    "/vector_addition_02",
    name="Vector Addition",
    nickname="VecAdd",
    description="Add two vectors",
    inputs=[
        hs.HopsPoint("Point A", "A", "First point"),
        hs.HopsPoint("Point B", "B", "Second point"),
        hs.HopsPoint("Point C", "C", "Third point"),
    ],
    outputs=[
        hs.HopsVector("Vector1", "V1", "First vector"),
        hs.HopsVector("Vector2", "V2", "Second vector"),
        hs.HopsVector("Vector", "V", "Resulting vector")
        ]
)
def vector_addition_02(a: rhino3dm.Point3d, b: rhino3dm.Point3d, c: rhino3dm.Point3d):
    vector1 = rhino3dm.Vector3d(b.X - a.X, b.Y - a.Y, b.Z - a.Z)
    vector2 = rhino3dm.Vector3d(c.X - b.X, c.Y - b.Y, c.Z - b.Z)
    vector3 = rhino3dm.Vector3d(vector1.X + vector2.X, vector1.Y + vector2.Y, vector1.Z + vector2.Z)
    return vector1, vector2, vector3

#tip-to-tail method of vector addition
#the resultant is the vector drawn from the tail of the first vector to the head of the last vector
#the resultant is the sum of the vectors
#three displacement vectors are added together to find the resultant displacement vector
#if we tip-to-tail add the vectors, in any order, the resultant displacement vector is the same
#example
#s = s1 + s2 + s3 = s2 + s1 + s3
#magnitude of the resultant displacement vector is the sum of the magnitudes of the displacement vectors
#absolute value of the resultant displacement vector is the sum of the absolute values of the displacement vectors

#write into @hops format
@hops.component(
    "/tip_to_tail_01",
    name="Tip to Tail",
    nickname="T2T",
    description="Add vectors tip to tail",
    inputs=[
        hs.HopsPoint("Point A", "A", "First point"),
        hs.HopsPoint("Point B", "B", "Second point"),
        hs.HopsPoint("Point C", "C", "Third point"),
    ],
    outputs=[
        hs.HopsVector("Vector1", "V1", "First vector"),
        hs.HopsVector("Vector2", "V2", "Second vector"),
        hs.HopsVector("Resultant Vector", "V", "Resulting vector")
        ]
)
def tip_to_tail_01(a: rhino3dm.Point3d, b: rhino3dm.Point3d, c: rhino3dm.Point3d):
    vector1 = rhino3dm.Vector3d(b.X - a.X, b.Y - a.Y, b.Z - a.Z)
    vector2 = rhino3dm.Vector3d(c.X - b.X, c.Y - b.Y, c.Z - b.Z)
    vector3 = rhino3dm.Vector3d(vector1.X + vector2.X, vector1.Y + vector2.Y, vector1.Z + vector2.Z)
    return vector1, vector2, vector3

#write into @hops format
@hops.component(
    "/tip_to_tail_02",
    name="Tip to Tail",
    nickname="T2T",
    description="Add vectors tip to tail",
    inputs=[
        hs.HopsPoint("Point A", "A", "First point"),
        hs.HopsPoint("Point B", "B", "Second point"),
        hs.HopsPoint("Point C", "C", "Third point"),
        hs.HopsPoint("Point D", "D", "Fourth point"),
    ],
    outputs=[
        hs.HopsVector("Vector1", "V1", "First vector"),
        hs.HopsVector("Vector2", "V2", "Second vector"),
        hs.HopsVector("Vector3", "V3", "Third vector"),
        hs.HopsVector("Resultant Vector", "V", "Resulting vector")
        ]
)
def tip_to_tail_01(a: rhino3dm.Point3d, b: rhino3dm.Point3d, c: rhino3dm.Point3d, d: rhino3dm.Point3d):
    vector1 = rhino3dm.Vector3d(b.X - a.X, b.Y - a.Y, b.Z - a.Z)
    vector2 = rhino3dm.Vector3d(c.X - b.X, c.Y - b.Y, c.Z - b.Z)
    vector3 = rhino3dm.Vector3d(d.X - c.X, d.Y - c.Y, d.Z - c.Z)
    vector4 = rhino3dm.Vector3d(vector1.X + vector2.X + vector3.X, vector1.Y + vector2.Y + vector3.Y, vector1.Z + vector2.Z + vector3.Z)
    return vector1, vector2, vector3, vector4

#Parallelogram Method of Vector Addition
#the resultant is the vector drawn from the tail of the first vector to the head of the last vector
#represented by the diagonal of the parallelogram
#draw the two vectors as adjacent sides of a parallelogram
#example
#s = s1 + s2 = s2 + s1
#write into @hops format
@hops.component(
    "/parallelogram_01",
    name="Parallelogram",
    nickname="Para",
    description="Add vectors using parallelogram method",
    inputs=[
        hs.HopsPoint("Point A", "A", "First point"),
        hs.HopsPoint("Point B", "B", "Second point"),
        hs.HopsPoint("Point C", "C", "Third point")
    ],
    outputs=[
        hs.HopsVector("Vector1", "V1", "First vector"),
        hs.HopsVector("Vector2", "V2", "Second vector"),
        hs.HopsVector("Resultant Vector", "V", "Resulting vector")
        ]
)
def parallelogram_01(a: rhino3dm.Point3d, b: rhino3dm.Point3d, c: rhino3dm.Point3d):
    vector1 = rhino3dm.Vector3d(b.X - a.X, b.Y - a.Y, b.Z - a.Z)
    vector2 = rhino3dm.Vector3d(c.X - a.X, c.Y - a.Y, c.Z - a.Z)
    vector3 = rhino3dm.Vector3d(vector1.X + vector2.X, vector1.Y + vector2.Y, vector1.Z + vector2.Z)
    return vector1, vector2, vector3


#Subtraction of Vectors
#the subtraction of vectors is called vector subtraction
#reverse the direction of the vector to be subtracted and add it to the first vector
#example
#s = s1 - s2 = s1 + (-s2)
#write into @hops format
@hops.component(
    "/vector_subtraction_03",
    name="Vector Subtraction",
    nickname="VecSub",
    description="Subtract two vectors",
    inputs=[
        hs.HopsPoint("Point A", "A", "First point"),
        hs.HopsPoint("Point B", "B", "Second point"),
        hs.HopsPoint("Point C", "C", "Third point")
    ],
    outputs=[
        hs.HopsVector("Vector1", "V1", "First vector"),
        hs.HopsVector("Vector2", "V2", "Second vector"),
        hs.HopsVector("Resultant Vector", "V", "Resulting vector")
        ]
)
def vector_subtraction_03(a: rhino3dm.Point3d, b: rhino3dm.Point3d, c: rhino3dm.Point3d):
    vector1 = rhino3dm.Vector3d(b.X - a.X, b.Y - a.Y, b.Z - a.Z)
    vector2 = rhino3dm.Vector3d(c.X - b.X, c.Y - b.Y, c.Z - b.Z)
    vector3 = rhino3dm.Vector3d(vector1.X - vector2.X, vector1.Y - vector2.Y, vector1.Z - vector2.Z)
    return vector1, vector2, vector3

#The Trigonometric Functions
#are defined in relation to a right triangle
#the three sides of a right triangle are the hypotenuse, the opposite side, and the adjacent side
#sin(theta) = opposite/hypotenuse
#cos(theta) = adjacent/hypotenuse
#tan(theta) = opposite/adjacent
#write into @hops format
@hops.component(
    "/trigonometric_functions_04",
    name="Trigonometric Functions",
    nickname="TrigFunc",
    description="Calculate trigonometric functions",
    inputs=[
        hs.HopsNumber("adjacent", "A", "Adjacent side"),
        hs.HopsNumber("opposite", "O", "Opposite side"),
        hs.HopsNumber("hypotenuse", "H", "Hypotenuse")
    ],
    outputs=[
        hs.HopsNumber("Sine", "S", "Sine of angle"),
        hs.HopsNumber("Cosine", "C", "Cosine of angle"),
        hs.HopsNumber("Tangent", "T", "Tangent of angle")
        ]
)
def trigonometric_functions_04(a: float, o: float, h: float):
    s = o/h
    c = a/h
    t = o/a
    return s, c, t

#A Component of a Vector
#the component of a vector is the projection of the vector onto a line
#the x component of a vector is the projection of the vector onto the x axis
#a vector in 3D space has three components, 
#the x component, the y component, and the z component
#example
#Rx = R cos(theta)
#Ry = R sin(theta)

#write into @hops format
@hops.component(
    "/vector_components_03",
    name="Vector Components",
    nickname="VecComp",
    description="Calculate vector components",
    inputs=[
        hs.HopsVector("vector", "R", "Vector"),
        hs.HopsNumber("length", "L", "Length of vector"),
        hs.HopsNumber("angle", "A", "Angle of vector")
    ],
    outputs=[
        hs.HopsNumber("x component", "X", "X component of vector"),
        hs.HopsNumber("y component", "Y", "Y component of vector")
        ]
)   
def vector_components_03(r: rhino3dm.Vector3d, l: float, a: float):
    import math
    Rx = l * math.cos(a)
    Ry = l * math.sin(a)
    return Rx, Ry

#Component Method of Vector Addition
#the component method of vector addition is used to add vectors that are not at right angles to each other
#the x components of the vectors are added together to find the x component of the resultant vector
#the y components of the vectors are added together to find the y component of the resultant vector
#the z components of the vectors are added together to find the z component of the resultant vector
#the resultant vector is the vector with the x, y, and z components
#example
#R = sqrt(Rx^2 + Ry^2 + Rz^2)
#theta = tan^-1(Ry/Rx)
#in 2D space, the z component is zero
#the angle of the resultant with the x axis can be found using the inverse tangent function
#theta = tan^-1(Ry/Rx)
#tan(theta) = Ry/Rx

#write into @hops format
@hops.component(
    "/component_method_08",
    name="Component Method",
    nickname="CompMeth",
    description="Add vectors using component method",
    inputs=[
        hs.HopsVector("Vector1", "V1", "First vector"),
        hs.HopsVector("Vector2", "V2", "Second vector"),
        hs.HopsVector("Vector3", "V3", "Third vector")
    ],
    outputs=[
        hs.HopsVector("Resultant Vector", "V", "Resulting vector")
        ]
)
def component_method_08(v1: rhino3dm.Vector3d, v2: rhino3dm.Vector3d, v3: rhino3dm.Vector3d):
    Rx = v1.X + v2.X + v3.X
    Ry = v1.Y + v2.Y + v3.Y
    Rz = v1.Z + v2.Z + v3.Z
    return rhino3dm.Vector3d(Rx, Ry, Rz)

#write into @hops format
@hops.component(
    "/component_method_09",
    name="Component Method",
    nickname="CompMeth",
    description="Add vectors using component method",
    inputs=[
        hs.HopsVector("Vector1", "V1", "First vector"),
        hs.HopsVector("Vector2", "V2", "Second vector"),
        hs.HopsVector("Vector3", "V3", "Third vector")
    ],
    outputs=[
        hs.HopsVector("Resultant Vector", "V", "Resulting vector")
        ]
)
def component_method_09(v1: rhino3dm.Vector3d, v2: rhino3dm.Vector3d, v3: rhino3dm.Vector3d):
    import math
    Rx = v1.X + v2.X + v3.X
    Ry = v1.Y + v2.Y + v3.Y
    Rz = v1.Z + v2.Z + v3.Z
    R = math.sqrt(Rx**2 + Ry**2 + Rz**2)
    theta = math.atan(Ry/Rx)
    return rhino3dm.Vector3d(Rx, Ry, Rz), R, theta
    
#unit vectors
#unit vectors are vectors with a magnitude of 1
#example
#i = 1i
#j = 1j
#k = 1k
#the unit vectors i, j, and k are used to represent the x, y, and z axes    

#write into @hops format
@hops.component(
    "/unit_vectors",
    name="Unit Vectors",
    nickname="UnitVec",
    description="Calculate unit vectors",
    inputs=[
        hs.HopsVector("vector", "V", "Vector")
    ],
    outputs=[
        hs.HopsVector("unit vector", "U", "Unit vector")
        ]
)
def unit_vectors(v: rhino3dm.Vector3d):
    import math
    R = math.sqrt(v.X**2 + v.Y**2 + v.Z**2)
    Rx = v.X/R
    Ry = v.Y/R
    Rz = v.Z/R
    return rhino3dm.Vector3d(Rx, Ry, Rz)

#Mathematical Operations with Units
#the unit terms must be carried along with the numerical values
#and must undergo the same mathematical operations as the numerical values
#quantities cannot be added or subtracted unless they have the same units
#they must be converted to the same units before they can be added or subtracted
#however quantities with different units can be multiplied or divided
#the units of the result are the product or quotient of the units of the quantities
#example
#(5 m)(2 s) = 10 m*s
#(5 m)/(2 s) = 2.5 m/s

#write into @hops format
@hops.component(
    "/mathematical_operations_with_units",
    name="Mathematical Operations",
    nickname="MathOp",
    description="Calculate mathematical operations with units",
    inputs=[
        hs.HopsNumber("length", "L", "Length"),
        hs.HopsNumber("time", "T", "Time")
    ],
    outputs=[
        hs.HopsNumber("speed", "S", "Speed")
        ]
)
def mathematical_operations_with_units(l: float, t: float):
    return l/t

#Problem solving Guide
#1. read the problem carefully
#2. draw a simple diagram
#3. put in all the given information
#4. identify the unknown quantity
#5. select the appropriate equation
#6. substitute the known values into the equation
#7. solve the equation for the unknown quantity
#8. check the answer
#9. write the answer in a complete sentence
#10. include the correct units
#11. do not round off until the final answer is obtained

#A toy train moves along a winding track at an average speed of 2.5 m/s.  
#How far will it travel in 4.00 minutes? 

#write into @hops format
@hops.component(
    "/toy_train_01",
    name="Toy Train",
    nickname="ToyTrn",
    description="Calculate distance traveled by toy train",
    inputs=[
        hs.HopsNumber("speed", "S", "Speed"),
        hs.HopsNumber("time", "T", "Time")
    ],
    outputs=[
        hs.HopsNumber("distance", "D", "Distance")
        ]
)
def toy_train_01(s: float, t: float):
    #the defining equation for average speed is v = d/t
    #d is in meters
    #t is in seconds
    #convert minutes to seconds
    #1 minute = 60 seconds
    l = s * t * 60
    return l

#A student driving a car travels 10.0 km in 30.0 minutes. 
#What is the student's average speed in m/s?

#write into @hops format
@hops.component(
    "/student_car_01",
    name="Student Car",
    nickname="StuCar",
    description="Calculate average speed of student driving car",   
    inputs=[
        hs.HopsNumber("distance", "D", "Distance"),
        hs.HopsNumber("time", "T", "Time")
    ],
    outputs=[
        hs.HopsNumber("speed", "S", "Speed")
        ]
)
def student_car_01(d: float, t: float):
    #the defining equation for average speed is v = d/t
    #d is in kilometers
    #t is in minutes
    #convert kilometers to meters
    #1 kilometer = 1000 meters
    #convert minutes to seconds
    #1 minute = 60 seconds
    v = (d * 1000)/(t * 60)
    return v

#Rollling along across the machine shop at a constant speed of S m/s,
#a robot covers a distance of D m. 
#How long does it take the robot to travel this distance?

#write into @hops format
@hops.component(
    "/robot_01",
    name="Robot",
    nickname="Rob",
    description="Calculate time taken by robot to travel distance",
    inputs=[
        hs.HopsNumber("speed", "S", "Speed"),
        hs.HopsNumber("distance", "D", "Distance")
    ],
    outputs=[
        hs.HopsNumber("time", "T", "Time")
        ]
)
def robot_01(s: float, d: float):
    #the defining equation for average speed is v = d/t
    #t = d/v
    t = d/s
    return t

#Change the speed S cm/s to units of kilometers per year. 
#Use 365 days in a year.

#write into @hops format
@hops.component(
    "/speed_04",
    name="Speed",
    nickname="Spd",
    description="Convert speed from cm/s to km/year",
    inputs=[
        hs.HopsNumber("speed", "S", "Speed")
    ],
    outputs=[
        hs.HopsNumber("speed", "S", "Speed")
        ]
)
def speed_04(s: float):
    #the defining equation for average speed is v = d/t
    #convert centimeters to kilometers
    #1 kilometer = 100000 centimeters
    #convert seconds into hours
    #convert hours into days
    #convert days into years
    #1 year = 365 days
    v = (s * 60 * 60 * 24 * 365)/100000
    return v

#A car travels along a road and its odometer readings are plotted
#against time in a Fig. 2-1. See notes for Fig. 2-1.
#Find the instantaneous speed of the car at points A and B. 
#What is the car's average speed?

#write into @hops format
@hops.component(
    "/car_01",
    name="Car",
    nickname="Car",
    description="Calculate instantaneous speed of car at points A and B",
    inputs=[
        hs.HopsNumber("distance", "D", "Distance"),
        hs.HopsNumber("time", "T", "Time")
    ],
    outputs=[
        hs.HopsNumber("speed", "S", "Speed")
        ]
)
def car_01(d: float, t: float):
    #the defining equation for average speed is v = d/t
    #d is in meters
    #t is in seconds
    #the slope is the change in distance divided by the change in time
    #we take the tangent to the curve at point A
    #from the diagram,
    #the change in distance/ the change in time = 4.0 m/8.0 s = 0.5 m/s
    #the slope at point A is 0.5 m/s
    #since the tangent line is the curve itself,
    #it is also the speed at point B and at every point along the curve
    #therefor the average speed is 0.5 m/s
    v = d/t
    return v

#A kid stands adj meters from the base of a flagpole which is opp meters tall.
#Determine the magnitude of the displacement of the brass eagle on top of the flagpole
#with respect to the kids feet

#write into @hops format
@hops.component(
    "/flagpole_01",
    name="Flagpole",
    nickname="Flgpl",
    description="Calculate magnitude of displacement of brass eagle on top of flagpole",
    inputs=[
        hs.HopsNumber("adjacent", "A", "Adjacent side"),
        hs.HopsNumber("opposite", "O", "Opposite side")
    ],
    outputs=[
        hs.HopsNumber("displacement", "D", "Displacement")
        ]
)
def flagpole_01(a: float, o: float):
    #the defining equation for displacement is d = xf - xi
    import math
    d = math.sqrt(a**2 + o**2)
    return d

#A runner makes one complete lap around a D m track in a time of T s.
#What were the runner's (a) average speed and (b) average velocity?

#write into @hops format
@hops.component(
    "/runner_01",
    name="Runner",
    nickname="Run",
    description="Calculate average speed and average velocity of runner",
    inputs=[
        hs.HopsNumber("distance", "D", "Distance"),
        hs.HopsNumber("time", "T", "Time")
    ],
    outputs=[
        hs.HopsNumber("speed", "S", "Speed"),
        hs.HopsNumber("velocity", "V", "Velocity")
        ]
)
def runner_01(d: float, t: float):
    #Average speed is the distance traveled divided by the time taken
    #Average velocity is the displacement divided by the time taken
    #since the run ends at the starting point, the displacement is zero
    #Average speed = Average velocity = d/t = 0/t = 0
    s = d/t
    v = 0/t
    return s, v

#Using the graphical method in Fig. 2-2 and Fig. 2-3,
#find the resultant of the following pairs of vectors
#the angles being taken relative to the +x axis, as is customary in physics
#Give your answer to two significant figures

#write into @hops format
@hops.component(
    "/graphical_method_02",
    name="Graphical Method",
    nickname="GraphMeth",
    description="Calculate resultant of vectors",
    inputs=[
        hs.HopsNumber("length1", "L1", "Length of first vector"),
        hs.HopsNumber("angle1", "A1", "Angle of first vector"),
        hs.HopsNumber("length2", "L2", "Length of second vector"),
        hs.HopsNumber("angle2", "A2", "Angle of second vector")
    ],
    outputs=[
        hs.HopsVector("Resultant Vector", "V", "Resulting vector"),
        hs.HopsNumber("magnitude", "M", "Magnitude of resulting vector"),
        hs.HopsNumber("angle", "A", "Angle of resulting vector")
        ]
)
def graphical_method_02(l1: float, a1: float, l2: float, a2: float):
    import math
    Rx = l1 * math.cos(a1) + l2 * math.cos(a2)
    Ry = l1 * math.sin(a1) + l2 * math.sin(a2)
    R = math.sqrt(Rx**2 + Ry**2)
    theta = math.atan(Ry/Rx)
    return rhino3dm.Vector3d(Rx, Ry, 0), R, theta

#Find the x- and y-components of a D meter displacement vector at 
#an angle of A degrees counterclockwise from the +x axis

#write into @hops format
@hops.component(
    "/displacement_01",
    name="Displacement",
    nickname="Disp",
    description="Calculate x and y components of displacement vector",
    inputs=[
        hs.HopsNumber("length", "L", "Length of vector"),
        hs.HopsNumber("angle", "A", "Angle of vector")
    ],
    outputs=[
        hs.HopsNumber("x component", "X", "X component of vector"),
        hs.HopsNumber("y component", "Y", "Y component of vector")
        ]
)
def displacement_01(l: float, a: float):
    import math
    Rx = l * math.cos(a)
    Ry = l * math.sin(a)
    return Rx, Ry

#where subtracting a vector is the same as adding the negative of the vector
#we simply reverse the direction of the vector to be subtracted and add it to the first vector
#the resultant is the vector drawn from the tail of the first vector to the head of the last vector
#represented by the diagonal of the parallelogram
#draw the two vectors as adjacent sides of a parallelogram
#example
#s = s1 + s2 = s2 + s1

#A boat can travel at a speed of v1 km/h in still water.
#In a flowing river, it can move v2 km/h relative to the water.
#If the river flows at a speed of v3 km/h, 
#how fast can the boat travel upstream?
#How fast can it travel downstream?

#write into @hops format
@hops.component(
    "/boat_01",
    name="Boat",
    nickname="Boat",
    description="Calculate speed of boat upstream and downstream",
    inputs=[
        hs.HopsNumber("speed1", "S1", "Speed of boat in still water"),
        hs.HopsNumber("speed2", "S2", "Speed of boat relative to water"),
        hs.HopsNumber("speed3", "S3", "Speed of river")
    ],
    outputs=[
        hs.HopsNumber("speed upstream", "Su", "Speed of boat upstream"),
        hs.HopsNumber("speed downstream", "Sd", "Speed of boat downstream")
        ]
)
def boat_01(s1: float, s2: float, s3: float):
    #the defining equation for average speed is v = d/t
    #the speed of the boat upstream is the speed of the boat in still water minus the speed of the river
    #the speed of the boat downstream is the speed of the boat in still water plus the speed of the river
    su = s1 - s3
    sd = s1 + s3
    return su, sd










































if __name__ == "__main__":
    app.run(debug=True)