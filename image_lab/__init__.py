"""
a library that implements all functionalities in the pixellab app, including gif making and the majority of functions of image editors that you know or you don't know about.

Created on Fri Aug  9 15:13:17 2024
project done by: ...

@author: Youssef Haddadi
        and: 

the idea is: using tkinter|pygame to create the GUI
editing an image then should pass through those steps
    * browsing your files to select an image to start editing
    * in case a folder is chosen, all images inside are modified
    * you can keep selecting different images to modify at a time
    * choose the modifications to apply and determine their arguments
    * hit the apply button
    * choose a path to register the modified image

note that
    ? mapping a pixel in an image is using the vw/vh units
    ? colors are supported in their rgb form
    ? there are shortcuts for each modification, they are all below this part
    ? i like how these comments are colored, 
        ? if u don't know what Im talking about,
        ? install "better comments" extension

shortcuts
    ! ...
    ! ...

"""



from .main import main