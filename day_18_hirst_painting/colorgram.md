# How colorgram can be used

```python
import colorgram

rgb_colors = []

# extracting 30 colors from image.jpg
colors = colorgram.extract('image.jpg', 30)

for color in colors:
     r = color.rgb.r
     g = color.rgb.g
     b = color.rgb.b
     new_color = (r, g, b)
     rgb_colors.append(new_color)

print(rgb_colors)
```