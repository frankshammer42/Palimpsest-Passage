# Development Proposal
This is a development proposal for Palimpsest Passage. The project will
be divided into three parts for development.
- Remove Background | Image Manipulation | Data Storage
- Camera Integration
- Arduino Integration

I think the overall project will take me 10-16 hours to finish. I will log out specific things I've done with
my working hours on Trello so that we are on the same page with the development process. My hourly rate is 50.
I'll start working on the project to create a time-line with specific milestones and share it with you, if we agree to move forward with it.
Please let me know if you have any question.

## Remove Background
I will first use openCV's [watershed algorithms](https://en.wikipedia.org/wiki/Watershed_(image_processing))
and [canny edge](https://en.wikipedia.org/wiki/Canny_edge_detector) to remove the background.
From my experiences, It's highly likely that the final algorithm will be a customised hybrid approach with
different algorithms to handle the specific hall way situation.

We can also use the [DeepLab](https://colab.research.google.com/github/tensorflow/models/blob/master/research/deeplab/deeplab_demo.ipynb) algorithm that uses machine learning to do semantic image segmentation. I don't think we
necessarily need to use this. But I think it's good that we have this option just in case the normal computer vision
algorithms are not working quite well in the setting

## Image Manipulation
[OpenCV](https://opencv.org/) provides all the necessary tools for image manipulation.
All the effects that you can find in Photoshop can be replicated with openCV (as long as it doesn't need any user input)

## Data Storage
We can use the normal file system to store and retrieve files. Since we are running python,
local files write and read should be a breeze to handle. If the access speed poses a bottle neck, we can
easily switch to [HDF5](https://www.hdfgroup.org/solutions/hdf5/) for fast access.

## Camera Integration
Depends on what cameras the project is gonna use, the difficulty varies. For simple Webcam, it is very straightforward to integrate it with Python. To integrate with Cannon/Nikon DSLR will require some
tweaks with USB3 port. I have friends who have done projects with the exact Python/DSLR setting so it won't be a problem if we are going for that setup.

## Arduino Integration
I will use [pyFirmata](https://pypi.org/project/pyFirmata/) to handle Arduino communication. The motion sensor will be connected to analog output pins on the Arduino board and the data will be directly read by the Python program to detect human movement. I used the library for several my
own ITP projects and the library proves to be very robust.
