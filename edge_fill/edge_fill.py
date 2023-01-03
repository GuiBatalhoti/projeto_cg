def edge_fill(image, x, y, fill_color, boundary_color):
  # Get the dimensions of the image
  width, height = image.size

  # Initialize the bounding box
  min_x, max_x, min_y, max_y = x, x, y, y

  # Initialize a stack with the starting point
  stack = [(x, y)]

  # Get the color of the starting point
  start_color = image.getpixel((x, y))

  # Check if the starting color is the same as the fill or boundary color
  if start_color == fill_color or start_color == boundary_color:
    return

  # Set the pixel at the starting point to the fill color
  image.putpixel((x, y), fill_color)

  # Define the directions to check
  directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

  # Iterate through the stack
  while stack:
    # Get the next point in the stack
    x, y = stack.pop()

    # Update the bounding box
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

    # Check the neighboring pixels
    for dx, dy in directions:
      # Calculate the coordinates of the neighboring pixel
      nx, ny = x + dx, y + dy

      # Check if the pixel is inside the image
      if 0 <= nx < width and 0 <= ny < height:
        # Get the color of the pixel
        color = image.getpixel((nx, ny))

        # Check if the pixel is the same color as the starting point and is not the boundary color
        if color == start_color and color != boundary_color:
          # Set the pixel to the fill color
          image.putpixel((nx, ny), fill_color)

          # Add the pixel to the stack
          stack.append((nx, ny))

  # Return the bounding box
  return (min_x, min_y, max_x, max_y)


from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

# Open an image file
image = Image.open("D:\Lucas\Documentos\projetoCG\circunferencia\projeto_cg\edge_fill/image.png")
fig, ax = plt.subplots(1, 2)
ax1, ax2 = ax.ravel()

# Convert the image to a mutable format
image = image.convert("RGB")
image.show(title = 'original image')





# Define the starting point, fill color, and boundary color
x, y = 300, 500
fill_color = (0, 0, 255)  # red
boundary_color = (255, 0, 0)  # blue

# Call the boundary fill function
bounding_box = edge_fill(image, x, y, fill_color, boundary_color)

# Print the bounding box
print(bounding_box)


# Save the modified image
image.save("D:\Lucas\Documentos\projetoCG\circunferencia\projeto_cg\edge_fill/filled_image.png")


draw = ImageDraw.Draw(image)
draw.rectangle(bounding_box, outline ="black", width=5)

image.show(title = 'filled image')
