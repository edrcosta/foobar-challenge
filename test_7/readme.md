Bringing a Gun to a Trainer Fight
=================================

## WRITE 

```javascript
    /**
     * @param {Array< width, height>} dimensions  
     * @param {Array<x, y>} your_position 
     * @param {Array<x, y>} trainer_position 
     * @param {Int} distance
     * 
     * @returns {Integer} 
     * number of distinct directions that you can fire to hit the elite trainer
     */
```

# ROOM 

> The walls reflect stuff 
> ROOM.dimensions === `[1 < x_dim <= 1250, 1 < y_dim <= 1250]`
> The room has integer dimensions

# people 

> positioned on the integer lattice 
> at different distinct positions
> PERSON.position === `[0 < x < x_dim, 0 < y < y_dim]`

# About the bean 
> DISTANCE <= 10000
> Beams travel a distance and stop
> Beams stop when hits you or the trainner

# example 

1. if you and the elite trainer positioned in a room with dimensions [3, 2]

> your_position [1, 1]
> trainer_position [2, 1]

```javascript
/**
 *    1  2  3   
 * 1 [E, 0, 0],
 * 2 [0, T, 0],
 */
```

2. maximum shot distance of 4

> shot distance = 4

3. you could shoot in seven different directions to hit the elite trainer 

> from your location! 
**vector bearings:**

[1, 0],
[1, 2],
[1, -2],
[3, 2],
[3, -2],
[-3, 2],
[-3, -2]

As specific examples, 

**[1, 0]**

1. is the straight line horizontal shot of distance 1

**[-3, -2]**

1. bounces off the left wall 
2. the bottom wall 
3. hitting the elite trainer

`total shot distance of sqrt(13)`

**[1, 2]**

2. bounces off just the top wall 
3. before hitting the elite trainer 

`total shot distance of sqrt(5)`

# Exercices 

solution([3,2], [1,1], [2,1], 4) == 7
solution([300,275], [150,150], [185,100], 500) == 9