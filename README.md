## Concavity Metrics
Repository to explore metrics to compare and mesure concavity in real data

I asumed that the x axe will always be time. The code is made in a way that any timescale works. 

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


Important things
- A column is the x axis
- B column is the y axis
- data for both stats on the row 2
- cell C1 is the start of the x axis
- cell D1 is the finish of the x axis
- needs to be the first worksheet
- you need to save the changes in the excel before geting the data
