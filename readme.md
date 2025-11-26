# Replicube Calculator

A calculator that provides the number of voxels present in a voxel set.

## Syntax

Empty set
```py
{}
```

1D set with coordinate $\langle 3 \rangle$
```py
{3}
```

1D set with coordinates $\{\langle 7 \rangle, \langle 9 \rangle\}$
```py
{7,9}
```

1D set with coordinates $\{\langle -2 \rangle, \dots, \langle 2 \rangle\}$ \
i.e. $\{\langle -2 \rangle, \langle -1 \rangle,\langle 0 \rangle,\langle 1 \rangle, \langle 2 \rangle\}$
```py
{-2,...,2}
```

2D set with coordinate $\langle 2,7 \rangle$
```py
{2}*{7}
```

2D set with coordinates
```math
\begin{bmatrix}
    \langle -2,-2 \rangle & \dots & \langle 2,-2 \rangle \\
    \vdots & \ddots & \vdots \\
    \langle -2,2 \rangle & \dots & \langle 2,2 \rangle \\
\end{bmatrix}
```
```py
{-2,...,2}*{-2,...,2}
```

3D set with coordinate $\langle 5,-6,1 \rangle$
```py
{5}*{-6}*{1}
```

3D set of a 5x5x5 cube
```py
{-2,...,2}*{-2,...,2}*{-2,...,2}
```

Union of sets $\{\langle 1 \rangle, \dots, \langle 3 \rangle\} \cup \{\langle -1 \rangle, \dots, \langle 2 \rangle\} = \{\langle -1 \rangle, \dots, \langle 3 \rangle\}$
```py
{1,...,3}|{-1,...,2}
```

Intersection of sets $\{\langle 1 \rangle, \dots, \langle 3 \rangle\} \cap \{\langle -1 \rangle, \dots, \langle 2 \rangle\} = \{\langle 1 \rangle, \dots, \langle 3 \rangle\}$
```py
{1,...,3}&{-1,...,2}
```

3D with union of 2D sets
```math
{\Big({\big(\underset{\text{cartesian product}}{\{-2, -2\} \times \{-1, \dots 3\}}\big)} \cup {\big(\{-2, \dots, 2\} \times \{-1, 3\}\big)}\Big)} \times \{3\}
```
```py
(({-2,2}*{-1,...,3})|({-2,...,2}*{-1,3}))*{-3}
```
