import bpy
from easybpy import *

# create cube
cube1 = create_cube()
# resize cube into flat surface 
scale(cube1, [4.5,5.0,1.0])

# create spheres 
sph1 = create_uv_sphere()
sph2 = create_uv_sphere()
sph3 = create_uv_sphere()
sph4 = create_uv_sphere()
sph5 = create_uv_sphere()
sph6 = create_uv_sphere()

# set locations
# 1st dot | upper left
location(sph1, [-2,3,1])
# 2nd dot | upper right
location(sph2, [2,3,1])
# 3rd dot | middle left
location(sph3, [-2,0,1])
# 4th dot | middle right
location(sph4, [2,0,1])
# 5th dot | bottom left
location(sph5, [-2,-3,1])
# 6th dot | bottom right
location(sph6, [2,-3,1])