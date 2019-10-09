#!bpy
"""
Name: 'template.py'
Blender: 2.76
Group: 'Sample'
Tooltip: 'Template for new scripts, copy it and start coding...'
"""
import bpy


def function_1():
    """ One line describing the task of this function """
    pass


def function_2():
    """ One line describing the task of this function """
    bpy.ops.mesh.primitive_cone_add(location=(0, 0, 4))


if __name__ == '__main__':
    # call the function for testing
    function_1()
    #function_2()