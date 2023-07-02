This got category 28 correct

```python
tf.keras.layers.Conv2D(32, 3, activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
tf.keras.layers.AveragePooling2D(pool_size=(2, 2)),
tf.keras.layers.Conv2D(32, 3, activation="relu"),
tf.keras.layers.AveragePooling2D(pool_size=(2, 2)),
tf.keras.layers.Flatten(),
tf.keras.layers.Dropout(0.5),
tf.keras.layers.Dense(NUM_CATEGORIES, activation="sigmoid")   
```

---

This did not get any correct

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

This did not get any correct

```python
tf.keras.layers.Conv2D(32, 3, activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
tf.keras.layers.Conv2D(64, 3, activation="relu"),
tf.keras.layers.AveragePooling2D(pool_size=(2, 2)),
tf.keras.layers.Flatten(),
tf.keras.layers.Dropout(0.5),
tf.keras.layers.Dense(NUM_CATEGORIES, activation="sigmoid")
```

---

This did not get any correct

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

This did not get any correct

```python
tf.keras.layers.Conv2D(32, 3, activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
tf.keras.layers.Conv2D(64, 3, activation="relu"),
tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
tf.keras.layers.Flatten(),
tf.keras.layers.Dropout(0.5),
tf.keras.layers.Dense(NUM_CATEGORIES, activation="sigmoid")
```

----

This got category 28 correct

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

This got categories 1 and 14 correct

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

This got categories 1, 14, and 28 correct

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