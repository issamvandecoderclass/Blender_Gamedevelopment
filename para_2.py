#!bpy
"""
Name: 'bprint-2.py'
Blender: 2.77
Group: 'Experiment'
Tooltip: 'Output of text in a scene'
"""
import bpy


def bprint():
    """Places a given text in the 3D view """

    bpy.ops.object.text_add(location=(0, 0, 0), rotation=(0, 0, 0))
    bpy.ops.object.editmode_toggle()
    bpy.ops.font.delete()
    bpy.ops.font.text_insert(text="If in doubt, just do it")
    bpy.ops.object.editmode_toggle()


def bprint_anothertext():
    """Places a given text in the 3D view """

    bpy.ops.object.text_add(location=(0, 0, 0), rotation=(0, 1, 0))
    bpy.ops.object.editmode_toggle()
    bpy.ops.font.delete()
    bpy.ops.font.text_insert(text="Making mistakes is part of it")
    bpy.ops.object.editmode_toggle()


if __name__ == '__main__':
    # Stop edit mode
    if bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode='OBJECT')

    # delete all mesh objects from a scene
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

    # delete all text objects from a scene
    bpy.ops.object.select_by_type(type='FONT')
    bpy.ops.object.delete()

    # call the new function
    bprint()
    bprint_anothertext()