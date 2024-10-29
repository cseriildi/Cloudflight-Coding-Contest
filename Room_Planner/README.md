# Room Planner

The goal is to calculate desk placements in various rooms according to specific constraints.

## Level 1

Each room is defined by its length (`x`) and width (`y`).
Desks cannot be stacked, and only 2D placement is allowed.
Desks are of size `1x3`, and the room’s length (`x`) is divisible by 3.

**Goal**:
  - Calculate the maximum number of desks that can fit in each room.
  - Output the maximum desk count per room.

## Level 2

The maximum number of tables is also provided.

**Goal**:
  - Output a matrix for each room where each cell contains the desk ID.

## Level 3

`x` may not be divisible by 3.

**Goal**:
  - Output a matrix for each room where each cell contains the desk ID.
  - Unused cells are marked as `0`.

## Level 4

Desks cannot touch each other but may touch walls.

**Goal**:
  - Output a matrix for each room.
  - Instead of the ID of the table mark them with `X` and empty cells with `.`.

## Level 5

Desks are now `1x2`

**Goal**:
  - Output a matrix for each room still using `X` and `.`.
