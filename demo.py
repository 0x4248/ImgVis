# ImgVis
# Visualize images with graphs
# Github: https://www.github.com/lewisevans2007/ImgVis
# Licence: GNU General Public License v3.0
# By: Lewis Evans
#
# This demo file tests the ImgVis module and shows how to use it
# This file is not required for the module to work



import ImgVis

demo_file = "test_img.jpeg"

ImgVis.colour_3d(demo_file, compression=50)
ImgVis.brightness_3d(demo_file, compression=50)
ImgVis.red_3d(demo_file, compression=50)
ImgVis.green_3d(demo_file, compression=50)
ImgVis.blue_3d(demo_file, compression=50)
ImgVis.red_line_2d(demo_file)
ImgVis.green_line_2d(demo_file)
ImgVis.blue_line_2d(demo_file)
ImgVis.combined_line_2d(demo_file)