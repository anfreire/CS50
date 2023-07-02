# Neural Network Optimization for Traffic Sign Classification


This document discusses the process of optimizing the layers of a neural network for traffic sign classification. The network was trained using data from the [German Traffic Sign Dataset](https://cdn.cs50.net/ai/2020/x/projects/5/gtsrb.zip).

&nbsp;

The initial network configuration was inspired by the one presented in [CS50's Introduction to AI with Python - Neural Networks - Lecture 5](https://youtu.be/J1QD9hLDEDY?t=4560).
A convolutional layer with 32 filters, a 3x3 kernel, ReLU activation function, and an input shape of `IMG_WIDTH` x `IMG_HEIGHT` for three color channels precedes a max pooling layer with a 2x2 pool size, a flatten layer, a hidden layer with 128 units and ReLU activation function, a hidden layer with 0.5 dropout rate, and an output layer with `NUM_CATEGORIES` units and softmax activation function. The Adam optimizer, categorical crossentropy loss function, and accuracy metric are used to build the model.

I began with:
- Starting loss: `5.1842`
- Starting accuracy: `0.0570`
- Ending loss: `3.4911`
- Ending accuracy: `0.0535`

Observations such as early loss and accuracy statistics, as well as ultimate loss and accuracy numbers, prompted the first adjustments. As part of the changes, certain layers, such as the MaxPooling, were relocated. Going back and forth from convultional layers with 32 to 64 filters and MaxPooling2D to AvaragePooling2d.

I ended up with: 
- Starting loss: `1.7920`
- Starting accuracy: `0.6548`
- Ending loss: `0.0504`
- Ending accuracy: `0.9872`

This network was made up of two Conv2D layers, each with 32 filters, a 3x3 kernel, a ReLU activation function, and an input shape of `IMG_WIDTH` x `IMG_HEIGHT` for three color channels, followed by an AvaragePooling2D layer with a 2x2 pool size, a flatten layer, a dropout layer, and a flatten layer. The model, like the initial model, is built with the Adam optimizer, categorical crossentropy loss function, and accuracy metric.

&nbsp;

The results were much better, but I felt compelled to verify the final configuration; the numbers studied are important, but they may not be the best method for evaluating the model.

So, I wrote a little program to run in an infinite loop so I could pass alternative images than the ones examined and observe how the model behaved.

<details>
  <summary>Test Program</summary>

  ```python
    import os
    import cv2
    import sys
    import numpy as np
    import tensorflow as tf

    IMG_WIDTH = 30
    IMG_HEIGHT = 30
    NUM_CATEGORIES = 43

    
    def main():
    # Ensure correct usage
    if (len(sys.argv) != 2):
      print("Usage: python3 test.py <model_path>")
      sys.exit(1)
    # Load the model
    model = tf.keras.models.load_model(sys.argv[1])
    try:
      while True:
      # Prompt user for image path
      image_path = input("Enter the path of the image to test (CTRL-C to exit): ")
      # Ensure image path is valid
      if not os.path.isfile(image_path):
          print("Invalid image path.")
          continue
      # Make prediction
      prediction = model.predict(np.reshape(cv2.resize(cv2.imread(image_path), (IMG_WIDTH, IMG_HEIGHT)), (1, IMG_WIDTH, IMG_HEIGHT, 3)))
      # Print result
      print("Predicted category index is: " + str(np.argmax(prediction)))
    # Handle keyboard interrupt
    except KeyboardInterrupt:
          print("\nExiting...")

    if __name__ == "__main__":
      main()
  ```
  </details>

&nbsp;
        

To test the models, I used three Google photos with signs from the 1, 14, and 28 categories.

<details>
  <summary>Test Images</summary>
  
  <img src="https://github.com/anfreire/CS50/blob/master/Introduction%20to%20Artificial%20Intelligence%20with%20Python/traffic/testing/testing_photos/CATEGORY_1.jpg?raw=true" alt="Image 1">
  <img src="https://github.com/anfreire/CS50/blob/master/Introduction%20to%20Artificial%20Intelligence%20with%20Python/traffic/testing/testing_photos/CATEGORY_14.jpg?raw=true" alt="Image 14">
  <img src="https://github.com/anfreire/CS50/blob/master/Introduction%20to%20Artificial%20Intelligence%20with%20Python/traffic/testing/testing_photos/CATEGORY_28.jpg?raw=true" alt="Image 28">
</details>

&nbsp;

I made multiple model compilations and tested the model with test photos.

<details>
  <summary>Tests Overview</summary>
  
  ### This got category 28 correct

  ```python
  tf.keras.layers.Conv2D(32, 3, activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
  tf.keras.layers.AveragePooling2D(pool_size=(2, 2)),
  tf.keras.layers.Conv2D(32, 3, activation="relu"),
  tf.keras.layers.AveragePooling2D(pool_size=(2, 2)),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dropout(0.5),
  tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
  ```

  ---

  ### This did not get any correct

  ```python
  tf.keras.layers.Conv2D(64, 3, activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
  tf.keras.layers.AveragePooling2D(pool_size=(2, 2)),
  tf.keras.layers.Conv2D(64, 3, activation="relu"),
  tf.keras.layers.AveragePooling2D(pool_size=(2, 2)),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dropout(0.5),
  tf.keras.layers.Dense(NUM_CATEGORIES, activation="sigmoid")
  ```

  ----

  ### This did not get any correct

  ```python
  tf.keras.layers.Conv2D(32, 3, activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
  tf.keras.layers.Conv2D(64, 3, activation="relu"),
  tf.keras.layers.AveragePooling2D(pool_size=(2, 2)),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dropout(0.5),
  tf.keras.layers.Dense(NUM_CATEGORIES, activation="sigmoid")
  ```

  ---

  ### This did not get any correct

  ```python
  tf.keras.layers.Conv2D(32, 3, activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
  tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
  tf.keras.layers.Conv2D(32, 3, activation="relu"),
  tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dropout(0.5),
  tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
  ```

  ---

  ### This did not get any correct

  ```python
  tf.keras.layers.Conv2D(32, 3, activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
  tf.keras.layers.Conv2D(64, 3, activation="relu"),
  tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dropout(0.5),
  tf.keras.layers.Dense(NUM_CATEGORIES, activation="sigmoid")
  ```

  ----

  ### This got category 28 correct

  ```python
  model = tf.keras.models.Sequential([
  tf.keras.layers.Conv2D(32, 3, activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
  tf.keras.layers.Dense(64, activation="relu"),
  tf.keras.layers.Conv2D(64, 3, activation="relu"),
  tf.keras.layers.Dense(128, activation="relu"),
  tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dropout(0.25),
  tf.keras.layers.Dense(NUM_CATEGORIES, activation="sigmoid")
  ])
  ```

  ---

  ### This got categories 1 and 14 correct

  ```python
  tf.keras.layers.Conv2D(32, 3, activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
  tf.keras.layers.Dense(32, activation="relu"),
  tf.keras.layers.Conv2D(64, 3, activation="relu"),
  tf.keras.layers.Dense(64, activation="relu"),
  tf.keras.layers.Conv2D(128, 3, activation="relu"),
  tf.keras.layers.Dense(128, activation="relu"),
  tf.keras.layers.AveragePooling2D(pool_size=(2, 2)),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dropout(0.25),
  tf.keras.layers.Dense(NUM_CATEGORIES, activation="sigmoid")
  ```

  ---

  ### This got categories 1, 14, and 28 correct

  ```python
  tf.keras.layers.Conv2D(32, 3, activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
  tf.keras.layers.Dense(32, activation="relu"),
  tf.keras.layers.AveragePooling2D(pool_size=(2, 2)),
  tf.keras.layers.Conv2D(64, 3, activation="relu"),
  tf.keras.layers.Dense(64, activation="relu"),
  tf.keras.layers.AveragePooling2D(pool_size=(2, 2)),
  tf.keras.layers.Conv2D(128, 3, activation="relu"),
  tf.keras.layers.Dense(128, activation="relu"),
  tf.keras.layers.AveragePooling2D(pool_size=(2, 2)),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dropout(0.25),
  tf.keras.layers.Dense(NUM_CATEGORIES, activation="sigmoid")
  ```
  </details>

&nbsp;

The final model had a `loss: 0.0409 - accuracy: 0.9909` and passed all of my tests; to achieve this, I used a different output activation function, the sigmoid, which performed better than the softmax. I also added more conv2d layers, followed by a dense layer with the same number of filters, followed by an avaragePooling layer that was repeated three times with the filters doubled each time.
I also preserved the 0.25 dropout because my experiments showed that it did not create overfitting. I am really pleased with the end result because it took less time than some of the tests and performed better than every other model I evaluated. 

The final setup is as follows:

```python
tf.keras.layers.Conv2D(32, 3, activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
tf.keras.layers.Dense(32, activation="relu"),
tf.keras.layers.AveragePooling2D(pool_size=(2, 2)),
tf.keras.layers.Conv2D(64, 3, activation="relu"),
tf.keras.layers.Dense(64, activation="relu"),
tf.keras.layers.AveragePooling2D(pool_size=(2, 2)),
tf.keras.layers.Conv2D(128, 3, activation="relu"),
tf.keras.layers.Dense(128, activation="relu"),
tf.keras.layers.AveragePooling2D(pool_size=(2, 2)),
tf.keras.layers.Flatten(),
tf.keras.layers.Dropout(0.25),
tf.keras.layers.Dense(NUM_CATEGORIES, activation="sigmoid")
```