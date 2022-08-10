## Concavity Metrics
Repository to explore metrics to compare and mesure concavity in real data


# Bigger distance between de curve and the start-finish line
The bigger distance between the curve and the start-finish line for each side. Normilized so its in proportion to the length of the start-finish line
```
big_dist, small_dist, big_dist_time, small_dist_time =  get_bigger_distance(start, finish, f_x)
```

# Second derivative
generates an array with the second derivative, but its not useful to compare diferent curves because the value its suceptible to noise. 
```
get_numerical_second_derivative(np.array(time), np.array(curve))
```

# Bigger and smaller angle
If its searched just the bigger angle, gives values next to the start or finish point. But if its taken the values in the points with bigger and smaller distance it can make a good metric to compare with other curves.

# Area upper and below the start-finish line
Get the area below and on top of the curve. Its good comparing curves with the same time intervals