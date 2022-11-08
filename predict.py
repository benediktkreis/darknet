#!/usr/bin/env python3

import os
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import glob



for filename in glob.glob('./test/test_images/*.jpg'):
  data_name = os.path.basename(filename)
  print('\nPredicting: ',data_name)
  # test each image, move the image with bounding box to your folder, and rename it
  # set code to paths: your yolo.data, your .cfg file, the model/weights you wanna use
  cmd = './darknet detector test ./test/yolov4.data test/yolov4x-mish-custom-test.cfg test/test_weights/yolov4x-mish-custom_best.weights '+filename+' -thresh 0.25 -dont_show'
  os.system(cmd)
  cmd = 'mv ./predictions.jpg ./test/predictions/thresh_25/'+data_name[:-4]+'_prediction_rel_bb_from0_thresh_25.jpg'
  os.system(cmd)
print('\nDone')