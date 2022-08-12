# Beziation

Bezier curves for pygame

## Usage

1. Import it
 ```python
 from beziation import bezier
 ```
2. Use it
 ```python
 bc = bezier(3, [(0, 0), (75, 100), (200, 100), (250, 200)])
 for x in range(0, len(points)-1):
    pygame.draw.line(win, color, points[x], points[x+1])
 ```