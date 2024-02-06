# ImgVis
# Visualize images with graphs
# Github: https://www.github.com/lewisevans2007/ImgVis
# Licence: GNU General Public License v3.0
# By: Lewis Evans

"""
# ImgVis

Visualize images with graphs

## Requiered packages
- Matplotlib - `pip install matplotlib`
- Pillow - `pip install pillow`
- Numpy - `pip install numpy`

## 3D Functions

Each function has the following parameters:
- image (str): The path to the image
- compression (int): The compression of the image. This is the times that the image is compressed. The higher the compression, the faster the function will run, but the less accurate the graph will be. The default value is 0 which means that the image will not be compressed.

### Colour 3D

![Demo](https://raw.githubusercontent.com/lewisevans2007/ImgVis/main/doc/colour_3d.png|width=400px)

Visualize the colour of the image in 3D space. The x-axis is the red channel, the y-axis is the green channel and the z-axis is the blue channel.

```python

import ImgVis

ImgVis.colour_3d("example.png", compression=10)
```

### Brightness 3D

![Demo](https://raw.githubusercontent.com/lewisevans2007/ImgVis/main/doc/brightness_3d.png|width=400px)

Visualize the brightness of the image in 3D space. The x-axis is the red channel, the y-axis is the green channel and the z-axis is the blue channel.

```python
import ImgVis

ImgVis.brightness_3d("example.png", compression=10)
```

### Red 3D

![Demo](https://raw.githubusercontent.com/lewisevans2007/ImgVis/main/doc/red_3d.png|width=400px)


Visualize the red channel of the image in 3D space. The x-axis is the red channel, the y-axis is the green channel and the z-axis is the blue channel.

```python
import ImgVis

ImgVis.red_3d("example.png", compression=10)
```

### Green 3D

![Demo](https://raw.githubusercontent.com/lewisevans2007/ImgVis/main/doc/green_3d.png|width=400px)

Visualize the green channel of the image in 3D space. The x-axis is the red channel, the y-axis is the green channel and the z-axis is the blue channel.

```python
import ImgVis

ImgVis.green_3d("example.png", compression=10)
```

### Blue 3D

![Demo](https://raw.githubusercontent.com/lewisevans2007/ImgVis/main/doc/blue_3d.png|width=400px)

Visualize the blue channel of the image in 3D space. The x-axis is the red channel, the y-axis is the green channel and the z-axis is the blue channel.

```python
import ImgVis

ImgVis.blue_3d("example.png", compression=10)
```

## 2D Functions

The 2D functions have the following parameters:
- image (str): The path to the image

### Red Line 2D

![Demo](https://raw.githubusercontent.com/lewisevans2007/ImgVis/main/doc/red_line_2d.png|width=400px)

Visualize the red channel of the image in 2D space. The x-axis is the red channel and the y-axis is the green channel.

```python
import ImgVis

ImgVis.red_line_2d("example.png")
```

### Green Line 2D

![Demo](https://raw.githubusercontent.com/lewisevans2007/ImgVis/main/doc/green_line_2d.png|width=400px)

Visualize the green channel of the image in 2D space. The x-axis is the red channel and the y-axis is the green channel.

```python
import ImgVis

ImgVis.green_line_2d("example.png")
```

### Blue Line 2D

![Demo](https://raw.githubusercontent.com/lewisevans2007/ImgVis/main/doc/blue_line_2d.png|width=400px)

Visualize the blue channel of the image in 2D space. The x-axis is the red channel and the y-axis is the green channel.

```python
import ImgVis

ImgVis.blue_line_2d("example.png")
```

### Combined Line 2D

![Demo](https://raw.githubusercontent.com/lewisevans2007/ImgVis/main/doc/combined_line_2d.png|width=400px)

Visualize the red, green and blue channel of the image in 2D space. The x-axis is the red channel and the y-axis is the green channel.

```python
import ImgVis

ImgVis.combined_line_2d("example.png")
```

## Licence

This project is licenced under the GNU General Public License v3.0. See the [LICENCE](LICENCE) file for more information.
"""

import os
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def colour_3d(image,compression=0):
    """Plots a 3D graph of the colour values in the image

    Args:
        image (string): The path to the image
        compression (int, optional): Compresses the image by this amount. Defaults to 0.
    """
    image = Image.open(image)

    # Image compression
    if compression != 0:
        image = image.resize((image.size[0]//compression,image.size[1]//compression))

    # Convert image data to a NumPy array and normalize the values to [0, 1]
    image_array = np.array(image) / 255.0
    
    # RGB Extract
    red_values = image_array[:, :, 0].flatten()
    green_values = image_array[:, :, 1].flatten()
    blue_values = image_array[:, :, 2].flatten()
    
    # Create a 3D scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot RGB values on the graph
    ax.scatter(red_values, green_values, blue_values, c=image_array.reshape(-1, 3), marker='o')
    
    # Set labels
    ax.set_xlabel('Red')
    ax.set_ylabel('Green')
    ax.set_zlabel('Blue')
    
    # Show the plot
    plt.show()

def brightness_3d(image,compression=0):
    """Plots a 3D graph of the brightness values in the image
    
    Args:
        image (string): The path to the image
        compression (int, optional): Compresses the image by this amount. Defaults to 0.
    """
    
    image = Image.open(image)
    
    # Image compression
    if compression != 0:
        image = image.resize((image.size[0]//compression,image.size[1]//compression))
    
    # Convert the image to grayscale (black and white)
    bw_image = image.convert('L')
    
    # Convert the black and white image to a NumPy array and normalize the values to [0, 1]
    bw_array = np.array(bw_image) / 255.0
    
    # Get the dimensions of the image
    height, width = bw_array.shape
    
    # Create arrays for X, Y, and Z values
    x_values = np.arange(width)
    y_values = np.arange(height)
    x_mesh, y_mesh = np.meshgrid(x_values, y_values)
    z_values = bw_array.flatten()
    
    # Create a 3D scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot X, Y, and Z values
    ax.scatter(x_mesh.flatten(), y_mesh.flatten(), z_values, c=z_values, cmap='gray', marker='o')
    
    # Set labels
    ax.set_xlabel('X (Pixel Location)')
    ax.set_ylabel('Y (Pixel Location)')
    ax.set_zlabel('Z (Brightness)')
    
    # Show the plot
    plt.show()

def red_3d(image,compression=0):
    """Plots a 3D graph of the red values in the image
    
    Args:
        image (string): The path to the image
        compression (int, optional): Compresses the image by this amount. Defaults to 0.
    """
    image = Image.open(image)
    
    # Image compression
    if compression != 0:
        image = image.resize((image.size[0]//compression,image.size[1]//compression))
    
    # Convert image data to a NumPy array and normalize the values to [0, 1]
    
    image_array = np.array(image) / 255.0
    # Extract RGB values from the normalized image array
    red_values = image_array[:, :, 0].flatten()
    # Get the dimensions of the image
    height, width = image_array.shape[0],image_array.shape[1]
    # Create arrays for X, Y, and Z values

    x_values = np.arange(width)
    y_values = np.arange(height)
    x_mesh, y_mesh = np.meshgrid(x_values, y_values)
    z_values = red_values
    # Create a 3D scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Plot X, Y, and Z values

    ax.scatter(x_mesh.flatten(), y_mesh.flatten(), z_values, c=z_values, cmap='Reds', marker='o')
    # Set labels
    ax.set_xlabel('X (Pixel Location)')
    ax.set_ylabel('Y (Pixel Location)')
    ax.set_zlabel('Z (Red)')

    # Show the plot
    plt.show()

def green_3d(image,compression=0):
    """Plots a 3D graph of the green values in the image
    
    Args:
        image (string): The path to the image
        compression (int, optional): Compresses the image by this amount. Defaults to 0.
    """
    image = Image.open(image)
    
    # Image compression
    if compression != 0:
        image = image.resize((image.size[0]//compression,image.size[1]//compression))
    
    # Convert image data to a NumPy array and normalize the values to [0, 1]
    
    image_array = np.array(image) / 255.0
    # Extract RGB values from the normalized image array
    green_values = image_array[:, :, 1].flatten()
    # Get the dimensions of the image
    height, width = image_array.shape[0],image_array.shape[1]
    # Create arrays for X, Y, and Z values

    x_values = np.arange(width)
    y_values = np.arange(height)
    x_mesh, y_mesh = np.meshgrid(x_values, y_values)
    z_values = green_values
    # Create a 3D scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Plot X, Y, and Z values

    ax.scatter(x_mesh.flatten(), y_mesh.flatten(), z_values, c=z_values, cmap='Greens', marker='o')
    # Set labels
    ax.set_xlabel('X (Pixel Location)')
    ax.set_ylabel('Y (Pixel Location)')
    ax.set_zlabel('Z (Green)')

    # Show the plot
    plt.show()

def blue_3d(image, compression=0):
    """Plots a 3D graph of the blue values in the image
    
    Args:
        image (string): The path to the image
        compression (int, optional): Compresses the image by this amount. Defaults to 0.
    """
    image = Image.open(image)
    
    # Image compression
    if compression != 0:
        image = image.resize((image.size[0]//compression,image.size[1]//compression))
    
    # Convert image data to a NumPy array and normalize the values to [0, 1]
    
    image_array = np.array(image) / 255.0
    # Extract RGB values from the normalized image array
    blue_values = image_array[:, :, 2].flatten()
    # Get the dimensions of the image
    height, width = image_array.shape[0],image_array.shape[1]
    # Create arrays for X, Y, and Z values

    x_values = np.arange(width)
    y_values = np.arange(height)
    x_mesh, y_mesh = np.meshgrid(x_values, y_values)
    z_values = blue_values
    # Create a 3D scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Plot X, Y, and Z values

    ax.scatter(x_mesh.flatten(), y_mesh.flatten(), z_values, c=z_values, cmap='Blues', marker='o')
    # Set labels
    ax.set_xlabel('X (Pixel Location)')
    ax.set_ylabel('Y (Pixel Location)')
    ax.set_zlabel('Z (Blue)')

    # Show the plot
    plt.show()

def red_line_2d(image):
    """Plots a 2D graph of the red values in the image

    Args:
        image (string): The path to the image
    """
    image = Image.open(image)
    # Convert image data to a NumPy array and normalize the values to [0, 1]
    image_array = np.array(image) / 255.0
    # Extract RGB values from the normalized image array
    red_values = image_array[:, :, 0].flatten()
    # Get the dimensions of the image
    height, width = image_array.shape[0],image_array.shape[1]
    # Create arrays for X, Y, and Z values
    x_values = np.arange(256)

    y_values = []
    for i in range(256):
        y_values.append(0)
    for i in red_values:
        y_values[int(i*255)] += 1
    # Create a 3D scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Plot X, Y, and Z values
    ax.plot(x_values,y_values, color="red")
    
    # Set labels
    ax.set_xlabel('Red')
    ax.set_ylabel('Amount of pixels')
    
    # Show the plot
    plt.show()

def green_line_2d(image):
    """Plots a 2D graph of the green values in the image

    Args:
        image (string): The path to the image
    """
    image = Image.open(image)
    # Convert image data to a NumPy array and normalize the values to [0, 1]
    image_array = np.array(image) / 255.0
    # Extract RGB values from the normalized image array
    green_values = image_array[:, :, 1].flatten()
    # Get the dimensions of the image
    height, width = image_array.shape[0],image_array.shape[1]
    # Create arrays for X, Y, and Z values
    x_values = np.arange(256)

    y_values = []
    for i in range(256):
        y_values.append(0)
    for i in green_values:
        y_values[int(i*255)] += 1
    # Create a 3D scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Plot X, Y, and Z values
    ax.plot(x_values,y_values, color="green")
    
    # Set labels
    ax.set_xlabel('Green')
    ax.set_ylabel('Amount of pixels')
    
    # Show the plot
    plt.show()

def blue_line_2d(image):
    """Plots a 2D graph of the blue values in the image

    Args:
        image (string): The path to the image
    """
    image = Image.open(image)
    # Convert image data to a NumPy array and normalize the values to [0, 1]
    image_array = np.array(image) / 255.0
    # Extract RGB values from the normalized image array
    blue_values = image_array[:, :, 2].flatten()
    # Get the dimensions of the image
    height, width = image_array.shape[0],image_array.shape[1]
    # Create arrays for X, Y, and Z values
    x_values = np.arange(256)

    y_values = []
    for i in range(256):
        y_values.append(0)
    for i in blue_values:
        y_values[int(i*255)] += 1
    # Create a 3D scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Plot X, Y, and Z values
    ax.plot(x_values,y_values, color="blue")
    
    # Set labels
    ax.set_xlabel('Blue')
    ax.set_ylabel('Amount of pixels')
    
    # Show the plot
    plt.show()

def combined_line_2d(image):
    """Plots a 2D graph of the red green and blue values in the image in one graph

    Args:
        image (string): The path to the image
    """
    image = Image.open(image)
    # Convert image data to a NumPy array and normalize the values to [0, 1]
    image_array = np.array(image) / 255.0
    # Extract RGB values from the normalized image array
    red_values = image_array[:, :, 0].flatten()
    green_values = image_array[:, :, 1].flatten()
    blue_values = image_array[:, :, 2].flatten()
    # Get the dimensions of the image
    height, width = image_array.shape[0],image_array.shape[1]
    # Create arrays for X, Y, and Z values
    x_values = np.arange(256)

    red_y_values = []
    for i in range(256):
        red_y_values.append(0)
    for i in red_values:
        red_y_values[int(i*255)] += 1

    green_y_values = []
    for i in range(256):
        green_y_values.append(0)
    for i in green_values:
        green_y_values[int(i*255)] += 1

    blue_y_values = []
    for i in range(256):
        blue_y_values.append(0)
    for i in blue_values:
        blue_y_values[int(i*255)] += 1
    # Create a 3D scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Plot X, Y, and Z values
    ax.plot(x_values,red_y_values, color="red")
    ax.plot(x_values,green_y_values, color="green")
    ax.plot(x_values,blue_y_values, color="blue")
    
    # Set labels
    ax.set_xlabel('Red Green and Blue')
    ax.set_ylabel('Amount of pixels')
    
    # Show the plot
    plt.show()