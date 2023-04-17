from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyForm
from .models import MyModel


from numpy import loadtxt
from keras.models import load_model
import numpy as np
from keras.models import Sequential
import keras.utils as image
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Conv2D, MaxPool2D
from keras.layers import Activation, Dropout, Flatten, Dense, Input




def index(request):
    context = {}
    if request.method == "POST":
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            # name = form.cleaned_data.get("Name")
            form.save()
            # name = 'Attiq'
            # img = form.cleaned_data.get("Picture")
            # obj = MyModel.objects.create(
            #                     title = name,
            #                     img = img
            #                     )
            # obj.save()
            # print(obj)
            
            imag = MyModel.objects.last()
            
            CNN_aug_new = Sequential()

            CNN_aug_new.add(Input(shape=(75, 75, 3)))

            #Specify a list of the number of filters for each convolutional layer

            for n_filters in [16,32, 64]:
                CNN_aug_new.add(Conv2D(n_filters,strides=(2, 2), kernel_size=3, activation='relu'))

            # Fill in the layer needed between our 2d convolutional layers and the dense layer
            CNN_aug_new.add(Flatten())

            #Specify the number of nodes in the dense layer before the output
            CNN_aug_new.add(Dense(128, activation='relu'))

            #Specify the output layer
            CNN_aug_new.add(Dense(2, activation='softmax'))
            
            #Compiling the model
            CNN_aug_new.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')

            CNN_aug_new.load_weights('model_weights.h5')

            img = image.load_img(str(imag.img),target_size=(75, 75))
            img = image.img_to_array(img)
            img = np.array([img])
            datagen = ImageDataGenerator(rescale=1/255)
            aug_iter = datagen.flow(img, batch_size=1)
            prediction=CNN_aug_new.predict(aug_iter)

            if np.argmax(prediction)==0:
                result = 'With_Mask'
            else:
                result = "Without_Mask"
                
            context = {'form': form,'result': result}
            
            return render(request, 'faceapp/index.html', context)
            # name = 'abc'
            # img = form.cleaned_data.get("Picture")
            # obj = MyModel.objects.create(
            #                     title = name,
            #                     img = img
            #                     )
            # obj.save()
            # print(obj)
    else:
        form = MyForm()
    context['form']= form
    return render(request, "faceapp/index.html", context)