# ImgVis
# Visualize images with graphs
# Github: https://www.github.com/lewisevans2007/ImgVis
# Licence: GNU General Public License v3.0
# By: Lewis Evans

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