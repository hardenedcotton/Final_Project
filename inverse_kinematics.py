from math import acos, atan2, cos, pi, sin, sqrt


def s(i):
    sum = 0
    for n in range(i):
        sum += theta[n]
    return sin(sum)


def c(i):
    sum = 0
    for n in range(i):
        sum += theta[n]
    return cos(sum)


a = [50, 25, 25]  # cm
theta = [0, 0, 0]  # rad


T1 = [[cos(theta[0]), -sin(theta[0]), 0],
      [sin(theta[0]), cos(theta[0]), 0],
      [0, 0, 1]]
T2 = [[cos(theta[1]), -sin(theta[1]), a[0]],
      [sin(theta[1]), cos(theta[1]), 0],
      [0, 0, 1]]
T3 = [[cos(theta[2]), -sin(theta[2]), a[1]],
      [sin(theta[2]), cos(theta[2]), 0],
      [0, 0, 1]]

T4 = [[1, 0, a[2]],
      [0, 1, 0],
      [0, 0, 1]]

T0 = [[c(2), -s(2), a[0]*c(0)+a[1]*c(1)+a[2]*c(2)],
      [s(2), c(2), a[0]*c(0)+a[1]*c(1)+a[2]*c(2)],
      [0, 0, 1]]


x = a[0]*cos(theta[0]) + a[1] * cos(theta[0] + theta[1]) + \
    a[2]*cos(theta[0] + theta[1] + theta[2])

y = a[0]*sin(theta[0]) + a[1] * sin(theta[0] + theta[1]) + \
    a[2]*sin(theta[0] + theta[1] + theta[2])

print(x, y)


x_desired = 50
y_desired = 50

distance_to_end_effector = sqrt(x_desired**2 + y_desired**2)

theta[0] = atan2(y_desired, x_desired)

# checkpoint #

# Calculate the angle of the third joint (theta[2])
# Using the law of cosines to find the angle at the third joint
cos_theta2 = (a[0]**2 + a[1]**2 - distance_to_end_effector **
              2) / (2 * a[0] * a[1]) % 1
print(cos_theta2)

theta[2] = acos(cos_theta2)

# Calculate the angle of the second joint (theta[1])
# Using the law of sines to find the angle at the second joint
sin_theta1 = (a[1] * sin(theta[2])) / distance_to_end_effector
cos_theta1 = (a[0] + a[1] * cos(theta[2])) / distance_to_end_effector
theta[1] = atan2(sin_theta1, cos_theta1)

# Convert the angles to degrees for a more intuitive result
theta_deg = [theta[0] * 180 / pi, theta[1] * 180 / pi, theta[2] * 180 / pi]

print("Joint angles (degrees):", theta_deg)
