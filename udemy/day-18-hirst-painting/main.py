import colorgram

colors = colorgram.extract('./hirst_painting.jpg', 6)

first_color = colors[0]

print(first_color)