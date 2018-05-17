#!usr/bin/env python
import os
import sys
import time
os.system('./openni && ./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights *.avi')
sleep(5)
os.system('./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights *.avi')
