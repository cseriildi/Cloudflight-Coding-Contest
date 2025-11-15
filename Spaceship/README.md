# Spaceship

The goal is to navigate a spaceship through space using movement sequences defined by "paces." Pace is time divided by distance.

## Level 1: Calculate Time

- The spaceship moves in **1D space** using movement sequences.
- A **pace is a positive integer** representing time per unit distance

**Goal:**

- Calculate the time it takes to complete a sequence

## Level 2: Calculate Final Position and Time

- The spaceship starts at position 0
- **Pace is now any number between -5 and 5.**
- The sign determines the direction.

|               |  |  |  |  |  |  |  |  |  |  |  |
|---------------|--|--|--|--|--|--|--|--|--|--|--|
|Pace           |-1|-2|-3|-4|-5| 0| 5| 4| 3| 2| 1|
|Units of Space |-1|-1|-1|-1|-1| 0| 1| 1| 1| 1| 1|
|Units of Time  | 1| 2| 3| 4| 5| 1| 5| 4| 3| 2| 1|

**Goal:**

- For each sequence, calculate the final position and total time

## Level 3: Generate Movement Sequence to Reach Station

- The spaceship must generate its own movement sequence to reach a given space station.
- Start at position 0, must reach target position exactly
- Each sequence must start and end with pace 0
- Can only gradually change pace: `-1 ⇆ -2 ⇆ -3 ⇆ -4 ⇆ -5 ⇆ 0 ⇄ 5 ⇄ 4 ⇄ 3 ⇄ 2 ⇄ 1`
- Must complete within the given time limit

**Goal:**

- Generate a valid movement sequence for each space station

## Level 4: Navigate 2D Space Optimally

- The spaceship now moves in **2D space** and must reach a station with **optimal time usage**.
- Spaceship starts at position (0, 0)
- X and Y movements are independent (separate sequences)
- Each sequence starts and ends with pace 0
- Both sequences must complete within the time limit
- Both sequences can take different amounts of time

**Goal:**

- Generate two sequences: one for X-direction and one for Y-direction with optimal time

## Level 5: Avoid Asteroid Collision

- Navigate to a space station while **avoiding an asteroid**.
- Asteroid size: 1x1
- Spaceship size: 1x1 with a square safety area of radius 2 around it
- Collision occurs if the asteroid penetrates the safety area

**Goal:**

- Generate valid X and Y sequences that reach the target station without collision
- Time limit is generous; an optimal solution is not required
