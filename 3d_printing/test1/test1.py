import bpy

# create cube
bpy.ops.mesh.primitive_cube_add()
# resize cube into flat surface
bpy.ops.transform.resize(value=(10,5,1))

# add some dots, 1st row
bpy.ops.mesh.primitive_uv_sphere_add(location=(-8,3,1))
bpy.ops.mesh.primitive_uv_sphere_add(location=(-5.5,3,1))
bpy.ops.mesh.primitive_uv_sphere_add(location=(-1.5,3,1))
bpy.ops.mesh.primitive_uv_sphere_add(location=(1,3,1))
bpy.ops.mesh.primitive_uv_sphere_add(location=(5,3,1))
bpy.ops.mesh.primitive_uv_sphere_add(location=(7.5,3,1))

# more dots, 2nd row
bpy.ops.mesh.primitive_uv_sphere_add(location=(-8,0,1))
bpy.ops.mesh.primitive_uv_sphere_add(location=(-5.5,0,1))
bpy.ops.mesh.primitive_uv_sphere_add(location=(-1.5,0,1))
bpy.ops.mesh.primitive_uv_sphere_add(location=(1,0,1))
bpy.ops.mesh.primitive_uv_sphere_add(location=(5,0,1))
bpy.ops.mesh.primitive_uv_sphere_add(location=(7.5,0,1))


# more dots, 3rd row
bpy.ops.mesh.primitive_uv_sphere_add(location=(-8,-3,1))
bpy.ops.mesh.primitive_uv_sphere_add(location=(-5.5,-3,1))
bpy.ops.mesh.primitive_uv_sphere_add(location=(-1.5,-3,1))
bpy.ops.mesh.primitive_uv_sphere_add(location=(1,-3,1))
bpy.ops.mesh.primitive_uv_sphere_add(location=(5,-3,1))
bpy.ops.mesh.primitive_uv_sphere_add(location=(7.5,-3,1))