import bpy
import os
from easybpy import *

# reset cursor to origin if not already
bpy.context.scene.cursor.location = (0.0,0.0,0.0)

# set filepath
path = "C:/Users/richa/Documents/GitHub/braille_translation/3d_printing/characters/"
character = "space.stl"

# change directory
import os
os.chdir("C:/Users/richa/Documents/GitHub/braille_translation/3d_printing/characters")

# input text 
with open("input.txt", "r") as f:
    text = f.readlines()
    print(text)

# character function
def braille_char(text):
    for char in text:
        char = char.lower()
        
        


## 1st row - max 10 characters
# import object
bpy.ops.import_mesh.stl(filepath=path+character)

# next object
bpy.ops.import_mesh.stl(filepath=path+character)
# select object
obj2 = active_object()
# translate object
translate_along_x(9, obj2)

# next object
bpy.ops.import_mesh.stl(filepath=path+character)
# select object
obj2 = active_object()
# translate object
translate_along_x(18, obj2)

# next object
bpy.ops.import_mesh.stl(filepath=path+character)
# select object
obj2 = active_object()
# translate object
translate_along_x(27, obj2)

# next object
bpy.ops.import_mesh.stl(filepath=path+character)
# select object
obj2 = active_object()
# translate object
translate_along_x(36, obj2)

# next object
bpy.ops.import_mesh.stl(filepath=path+character)
# select object
obj2 = active_object()
# translate object
translate_along_x(45, obj2)

# next object
bpy.ops.import_mesh.stl(filepath=path+character)
# select object
obj2 = active_object()
# translate object
translate_along_x(54, obj2)

# next object
bpy.ops.import_mesh.stl(filepath=path+character)
# select object
obj2 = active_object()
# translate object
translate_along_x(63, obj2)

# next object
bpy.ops.import_mesh.stl(filepath=path+character)
# select object
obj2 = active_object()
# translate object
translate_along_x(72, obj2)

# next object
bpy.ops.import_mesh.stl(filepath=path+character)
# select object
obj2 = active_object()
# translate object
translate_along_x(81, obj2)

## 2nd row - max 10 characters
# next object
bpy.ops.import_mesh.stl(filepath=path+character)
# select object
obj2 = active_object()
# translate object
translate_along_y(-10, obj2)

# next object
bpy.ops.import_mesh.stl(filepath=path+character)
# select object
obj2 = active_object()
# translate object
translate_along_y(-10, obj2)
translate_along_x(9, obj2)

# next object
bpy.ops.import_mesh.stl(filepath=path+character)
# select object
obj2 = active_object()
# translate object
translate_along_y(-10, obj2)
translate_along_x(18, obj2)

# next object
bpy.ops.import_mesh.stl(filepath=path+character)
# select object
obj2 = active_object()
# translate object
translate_along_y(-10, obj2)
translate_along_x(27, obj2)

# next object
bpy.ops.import_mesh.stl(filepath=path+character)
# select object
obj2 = active_object()
# translate object
translate_along_y(-10, obj2)
translate_along_x(36, obj2)

# next object
bpy.ops.import_mesh.stl(filepath=path+character)
# select object
obj2 = active_object()
# translate object
translate_along_y(-10, obj2)
translate_along_x(45, obj2)

# next object
bpy.ops.import_mesh.stl(filepath=path+character)
# select object
obj2 = active_object()
# translate object
translate_along_y(-10, obj2)
translate_along_x(54, obj2)

# next object
bpy.ops.import_mesh.stl(filepath=path+character)
# select object
obj2 = active_object()
# translate object
translate_along_y(-10, obj2)
translate_along_x(63, obj2)

# next object
bpy.ops.import_mesh.stl(filepath=path+character)
# select object
obj2 = active_object()
# translate object
translate_along_y(-10, obj2)
translate_along_x(72, obj2)

# next object
bpy.ops.import_mesh.stl(filepath=path+character)
# select object
obj2 = active_object()
# translate object
translate_along_y(-10, obj2)
translate_along_x(81, obj2)



## post-process objects together

# select all objects 
select_all_objects()

# join objects
bpy.ops.object.join()

# export stl
# if permission denied error, can export file manually (File -> Export -> Stl)
export_path = path
bpy.ops.export_mesh.stl(filepath=export_path)
