#! bpy
"""
Name: 'halma_figure.py'
Blender: 2.77
Group: 'Example composit piece'
Tooltip: 'Create and add a halma figure'
"""
import bpy


def halma_figure():
    '''Create a halma figure from a ball and a cone'''
    # get the context
    scn = bpy.context.scene

    # names of the parts
    parts = ['head', 'body', 'halma_figure']

    # create the head
    bpy.ops.mesh.primitive_uv_sphere_add(location=(2, 2, .9))
    obj = bpy.context.object
    # scale the object on the x-, y-, and z-axis
    obj.scale[0] = .6
    obj.scale[1] = .6
    obj.scale[2] = .6
    # give the object the name head
    obj.name = parts[0]
    # make this object the active object
    scn.objects.active = scn.objects[parts[0]]

    # create the body
    bpy.ops.mesh.primitive_cone_add(location=(2, 2, 0))
    obj = bpy.context.object
    # scale the object on the x-, y-axis
    obj.scale[0] = .8
    obj.scale[1] = .8
    # give the object the name body
    obj.name = parts[1]
    # make this object the active object
    scn.objects.active = scn.objects[parts[1]]
    
    # connect parts to a new one
    scn.objects[parts[0]].select = True
    scn.objects[parts[1]].select = True
    bpy.ops.object.join()
    obj.name = parts[2]


if __name__ == '__main__':
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()
    halma_figure()