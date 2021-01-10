from keras.layers import Layer
from keras_contrib.layers.normalization.instancenormalization import InstanceNormalization, InputSpec
from keras.models import model_from_json
from PIL import Image
import numpy as np
import json
import tensorflow as tf


# reflection padding source
# https://github.com/fastai/courses/blob/master/deeplearning2/neural-style.ipynb
class ReflectionPadding2D(Layer):
    def __init__(self, padding=(1, 1), **kwargs):
        self.padding = tuple(padding)
        self.input_spec = [InputSpec(ndim=4)]
        super(ReflectionPadding2D, self).__init__(**kwargs)

    def compute_output_shape(self, s):
        return (s[0], s[1] + 2 * self.padding[0], s[2] + 2 * self.padding[1], s[3])

    def call(self, x, mask=None):
        w_pad, h_pad = self.padding
        return tf.pad(x, [[0, 0], [h_pad, h_pad], [w_pad, w_pad], [0, 0]], 'REFLECT')

def transform_image(path_to_neutral,emotion):
    path_to_model = 'models/neutral_'+emotion+'/model.json'
    path_to_weights = 'models/neutral_'+emotion+'/weights.hdf5'

    with open(path_to_model, 'r') as json_file:
        architecture = json.load(json_file)
    model = model_from_json(architecture, custom_objects={'ReflectionPadding2D': ReflectionPadding2D,'InstanceNormalization': InstanceNormalization})

    model.load_weights(path_to_weights)
    image = np.array(Image.open(path_to_neutral))

    arr = []
    image = image[:, :, np.newaxis]

    image = image/ 255
    arr.append(image)
    arr2=np.array(arr)
    synth_A = model.predict(arr2, batch_size=1)
    synth_A = synth_A[0][:, :, 0]
    synth_A = synth_A * (255)
    to_save=synth_A
    Image.fromarray(to_save.astype('uint8')).save('tmp/modified.png')
    return('tmp/modified.png')

if __name__ == '__main__':
    transform_image()
