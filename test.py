import keras.layers as KL
from keras.models import Model

layer_type='Dense'

in_lay = KL.Input(shape=(32,))
net=eval('KL.'+layer_type)(16)(in_lay)
model=Model(inputs=in_lay,outputs=net)
print(model.summary())