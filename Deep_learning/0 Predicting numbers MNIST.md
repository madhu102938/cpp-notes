## Importing all the libraries
```python
import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow import keras
import matplotlib.pyplot as plt
```

---
## Importing the Training and testing data
```python
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
len(x_train)
```

---
## Printing the image
```python
plt.imshow(x_train[0])
```

---
## Creating neural networks
```python
model = keras.Sequential([
    # input layer
    keras.layers.Dense(100, input_shape=(784,), activation='sigmoid'),

    # hidden layer
    keras.layers.Dense(100, activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(100, activation='relu'),
	keras.layers.Dropout(0.2),

    # output layer
    keras.layers.Dense(10, activation='sigmoid')
])
```

```python
keras.layers.Dense(units, activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)
```

- units - tells us number of neurons in the current layer

> [!NOTE] Neurons in input layer
> Sometimes, shape of the input layer and the number of neurons do not match just like in the above code, that just means, 784 features of the data are matched with the 100 neurons

[[0.1 Dropout layers]]

Gives a summary of our neural network, like number of neurons in each layer
```python
model.summary()
```

We need to compile the network before training our data
```python
model.compile(
    optimizer = 'adam',
    loss = 'sparse_categorical_crossentropy',
    metrics = ['accuracy']
)
```

1. **Optimizer (`optimizer='adam'`):**
    - The optimizer is the algorithm used to update the model's weights during training. `'adam'` is a popular optimization algorithm that combines ideas from RMSprop and momentum. It is known for its efficiency and adaptability to different types of data and tasks.
    - Other commonly used optimizers include `'sgd'` (Stochastic Gradient Descent), `'rmsprop'` (Root Mean Square Propagation), and others.

2. **Loss Function (`loss='sparse_categorical_crossentropy'`):**
	- Basically the cost function we use
    - The loss function is a measure of how well the model is performing. `'sparse_categorical_crossentropy'` is often used for classification problems where the target labels are integers (e.g., for multi-class classification tasks).
    - For binary classification, `'binary_crossentropy'` is commonly used. For regression tasks, mean squared error (`'mse'`) or mean absolute error (`'mae'`) may be used.

3. **Metrics (`metrics=['accuracy']`):**    
    - Metrics are used to monitor the performance of the model during training. `'accuracy'` is a commonly used metric for classification problems. It represents the proportion of correctly classified instances.
    - Additional metrics can be added to the list, such as `'precision'`, `'recall'`, or custom metrics based on the specific requirements of your task.

Our data needs to be of the same size of the `input_shape` mentioned in the neural networks creation code
```python
x_train.reshape(60000, 784)
```

---
## One Hot Encoding the data
```python
y_train = keras.utils.to_categorical(y_train, num_classes=10)
```
We can OneHotEncode our data, but we are using `sparse_categorical_crossentropy`, so it won't be necessary, but if we OneHotEncode the data, then we should `mean_squared_error`

- Here our output layer is 10 neurons size, but our `y_train` contains only 1 integer as the answer, so we should either
- OneHotEncode the data and use `mean_squared_error`, or
- we can directly use `sparse_categorical_crossentropy` and it will handle everything

---

```python
x_train_flatten = x_train.reshape(60_000, 784)
x_test_flatten = x_test.reshape(len(x_test), 784)

x_train_flatten = x_train_flatten/255
x_test_flatten = x_test_flatten / 255

model.fit(x_train_flatten, y_train, epochs=10)
```

We are training the model batch wise, we are using stochastic gradient descent
[[0.2 GD vs SDG]]

Here are we normalizing the data, so we can train the model faster and reach global minima faster 
[[0.3 Normalization vs activation]]

---

Hyper Parameter tuning : )
## Predicting from model

```python
predicted_data = model.predict(x_test_flatten)
```

- We **cannot** predict just one result, it has to be an array of values
- To predict just one value, we just instead pass on a slice of array

```python
one_predicted_data = model.predict(x_test_flatten[0:1])
```

- The array that is returned to us, contains likelihood for each result, maximum value of in array should be the predicted value
- To get the maximum value in a numpy array we use `argmax` function

```python
final_predicted_data = [np.argmax(i) for i in predicted_data]
```

---
## Confusion matrix

![confusion matrix](https://onestopdataanalysis.com/wp-content/uploads/2020/02/confusion_matrix.png)


```python
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, final_predicted_data))
```
