#!/usr/bin/python

import time
import keras_ocr
import matplotlib.pyplot as plt

pipeline = keras_ocr.pipeline.Pipeline()

images = [
    keras_ocr.tools.read(img) for img in ['Image1.jpg'
                                          
    ]
]

st = time.time()
prediction_groups = pipeline.recognize(images)

#fig, axs = plt.subplots(nrows=len(images), figsize=(10, 20))
#for ax, image, predictions in zip(axs, images, prediction_groups):
#    keras_ocr.tools.drawAnnotations(image=image, 
#                                    predictions=predictions, 
#
#                                    ax=ax)

predicted_image_1 = prediction_groups[0]
  for text, box in predicted_image_1:
    print(text)


et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')

