import os
import cv2
import sys
import numpy as np
import tensorflow as tf

IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43

    
def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 test.py <model_path>")
        sys.exit(1)
    model = tf.keras.models.load_model(sys.argv[1])
    try:
        while True:
            image_path = input("Enter the path of the image to test (CTRL-C to exit): ")
            if not os.path.isfile(image_path):
                print("Invalid image path.")
                continue
            prediction = model.predict(np.reshape(cv2.resize(cv2.imread(image_path), (IMG_WIDTH, IMG_HEIGHT)), (1, IMG_WIDTH, IMG_HEIGHT, 3)))
            print("Predicted category index is: " + str(np.argmax(prediction)))
    except KeyboardInterrupt:
        print("\nExiting...")
        
if __name__ == "__main__":
    main()
    