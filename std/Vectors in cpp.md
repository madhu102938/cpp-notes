
# Vectors in C++

## Introduction

A vector is a dynamic array in C++ that can be resized during runtime. It is a part of the Standard Template Library (STL) and is defined in the `<vector>` header file.

## Declaration

A vector can be declared in the following way:

```cpp
std::vector<datatype> vectorName;
```

For example:

```cpp
std::vector<int> myVector;
```

## Initialization

A vector can be initialized in the following ways:

### 1. Default Initialization

A vector can be initialized with default values using the following syntax:

```cpp
std::vector<datatype> vectorName(size);
```

For example:

```cpp
std::vector<int> myVector(5); // Initializes a vector of size 5 with default value 0
```

### 2. Initialization with Values

A vector can be initialized with values using the following syntax:

```cpp
std::vector<datatype> vectorName = {value1, value2, value3, ...};
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5}; // Initializes a vector with values 1, 2, 3, 4, 5
```

### 3. Initialization with Another Vector

A vector can be initialized with another vector using the following syntax:

```cpp
std::vector<datatype> vectorName(anotherVector);
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
std::vector<int> anotherVector(myVector); // Initializes another vector with the values of myVector
```

## Accessing Elements

Elements in a vector can be accessed using the following methods:

### 1. Using the [] Operator

Elements in a vector can be accessed using the [] operator and the index of the element. The index starts from 0.

```cpp
vectorName[index];
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
std::cout << myVector[0]; // Outputs 1
```

### 2. Using the at() Function

Elements in a vector can also be accessed using the at() function and the index of the element. The index starts from 0.

```cpp
vectorName.at(index);
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
std::cout << myVector.at(0); // Outputs 1
```

### 3. Using the front() Function

The front() function returns the first element of the vector.

```cpp
vectorName.front();
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
std::cout << myVector.front(); // Outputs 1
```

### 4. Using the back() Function

The back() function returns the last element of the vector.

```cpp
vectorName.back();
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
std::cout << myVector.back(); // Outputs 5
```

## Modifying Elements

Elements in a vector can be modified using the following methods:

### 1. Using the [] Operator

Elements in a vector can be modified using the [] operator and the index of the element. The index starts from 0.

```cpp
vectorName[index] = newValue;
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
myVector[0] = 10;
std::cout << myVector[0]; // Outputs 10
```

### 2. Using the at() Function

Elements in a vector can also be modified using the at() function and the index of the element. The index starts from 0.

```cpp
vectorName.at(index) = newValue;
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
myVector.at(0) = 10;
std::cout << myVector.at(0); // Outputs 10
```

### 3. Using the push_back() Function

The push_back() function adds a new element to the end of the vector.

```cpp
vectorName.push_back(newValue);
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
myVector.push_back(6);
std::cout << myVector.back(); // Outputs 6
```

### 4. Using the pop_back() Function

The pop_back() function removes the last element from the vector.

```cpp
vectorName.pop_back();
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
myVector.pop_back();
std::cout << myVector.back(); // Outputs 4
```

### 5. Using the insert() Function

The insert() function inserts a new element at a specified position in the vector.

```cpp
vectorName.insert(iterator, newValue);
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
auto it = myVector.begin() + 2;
myVector.insert(it, 10);
std::cout << myVector[2]; // Outputs 10
```

### 6. Using the erase() Function

The erase() function removes an element from the vector at a specified position.

```cpp
vectorName.erase(iterator);
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
auto it = myVector.begin() + 2;
myVector.erase(it);
std::cout << myVector[2]; // Outputs 4
```

## Size and Capacity

The size of a vector is the number of elements it contains. The capacity of a vector is the number of elements it can hold without reallocating memory.

### 1. Using the size() Function

The size() function returns the number of elements in the vector.

```cpp
vectorName.size();
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
std::cout << myVector.size(); // Outputs 5
```

### 2. Using the capacity() Function

The capacity() function returns the number of elements the vector can hold without reallocating memory.

```cpp
vectorName.capacity();
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
std::cout << myVector.capacity(); // Outputs 5
```

### 3. Using the reserve() Function

The reserve() function reserves memory for a specified number of elements in the vector.

```cpp
vectorName.reserve(numberOfElements);
```

For example:

```cpp
std::vector<int> myVector;
myVector.reserve(10);
std::cout << myVector.capacity(); // Outputs 10
```

## Iterators

Iterators are used to traverse the elements of a vector.

### 1. Using the begin() Function

The begin() function returns an iterator to the first element of the vector.

```cpp
vectorName.begin();
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
auto it = myVector.begin();
std::cout << *it; // Outputs 1
```

### 2. Using the end() Function

The end() function returns an iterator to the element following the last element of the vector.

```cpp
vectorName.end();
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
auto it = myVector.end() - 1;
std::cout << *it; // Outputs 5
```

### 3. Using the rbegin() Function

The rbegin() function returns a reverse iterator to the last element of the vector.

```cpp
vectorName.rbegin();
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
auto it = myVector.rbegin();
std::cout << *it; // Outputs 5
```

### 4. Using the rend() Function

The rend() function returns a reverse iterator to the element preceding the first element of the vector.

```cpp
vectorName.rend();
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
auto it = myVector.rend() - 1;
std::cout << *it; // Outputs 1
```

## Sorting

The sort() function is used to sort the elements of a vector in ascending order.

```cpp
std::sort(vectorName.begin(), vectorName.end());
```

For example:

```cpp
std::vector<int> myVector = {5, 4, 3, 2, 1};
std::sort(myVector.begin(), myVector.end());
for (auto i : myVector)
    std::cout << i << " "; // Outputs 1 2 3 4 5
```

## Conclusion

Vectors are a powerful data structure in C++ that can be used to store and manipulate collections of elements. With the functions and methods provided by the STL, vectors can be easily initialized, accessed, modified, and sorted.GitHub Copilot: Sure, here is an in-depth cheat sheet for vectors in C++:

# Vectors in C++

## Introduction

A vector is a dynamic array in C++ that can be resized during runtime. It is a part of the Standard Template Library (STL) and is defined in the `<vector>` header file.

## Declaration

A vector can be declared in the following way:

```cpp
std::vector<datatype> vectorName;
```

For example:

```cpp
std::vector<int> myVector;
```

## Initialization

A vector can be initialized in the following ways:

### 1. Default Initialization

A vector can be initialized with default values using the following syntax:

```cpp
std::vector<datatype> vectorName(size);
```

For example:

```cpp
std::vector<int> myVector(5); // Initializes a vector of size 5 with default value 0
```

### 2. Initialization with Values

A vector can be initialized with values using the following syntax:

```cpp
std::vector<datatype> vectorName = {value1, value2, value3, ...};
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5}; // Initializes a vector with values 1, 2, 3, 4, 5
```

### 3. Initialization with Another Vector

A vector can be initialized with another vector using the following syntax:

```cpp
std::vector<datatype> vectorName(anotherVector);
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
std::vector<int> anotherVector(myVector); // Initializes another vector with the values of myVector
```

## Accessing Elements

Elements in a vector can be accessed using the following methods:

### 1. Using the [] Operator

Elements in a vector can be accessed using the [] operator and the index of the element. The index starts from 0.

```cpp
vectorName[index];
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
std::cout << myVector[0]; // Outputs 1
```

### 2. Using the at() Function

Elements in a vector can also be accessed using the at() function and the index of the element. The index starts from 0.

```cpp
vectorName.at(index);
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
std::cout << myVector.at(0); // Outputs 1
```

### 3. Using the front() Function

The front() function returns the first element of the vector.

```cpp
vectorName.front();
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
std::cout << myVector.front(); // Outputs 1
```

### 4. Using the back() Function

The back() function returns the last element of the vector.

```cpp
vectorName.back();
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
std::cout << myVector.back(); // Outputs 5
```

## Modifying Elements

Elements in a vector can be modified using the following methods:

### 1. Using the [] Operator

Elements in a vector can be modified using the [] operator and the index of the element. The index starts from 0.

```cpp
vectorName[index] = newValue;
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
myVector[0] = 10;
std::cout << myVector[0]; // Outputs 10
```

### 2. Using the at() Function

Elements in a vector can also be modified using the at() function and the index of the element. The index starts from 0.

```cpp
vectorName.at(index) = newValue;
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
myVector.at(0) = 10;
std::cout << myVector.at(0); // Outputs 10
```

### 3. Using the push_back() Function

The push_back() function adds a new element to the end of the vector.

```cpp
vectorName.push_back(newValue);
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
myVector.push_back(6);
std::cout << myVector.back(); // Outputs 6
```

### 4. Using the pop_back() Function

The pop_back() function removes the last element from the vector.

```cpp
vectorName.pop_back();
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
myVector.pop_back();
std::cout << myVector.back(); // Outputs 4
```

### 5. Using the insert() Function

The insert() function inserts a new element at a specified position in the vector.

```cpp
vectorName.insert(iterator, newValue);
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
auto it = myVector.begin() + 2;
myVector.insert(it, 10);
std::cout << myVector[2]; // Outputs 10
```

### 6. Using the erase() Function

The erase() function removes an element from the vector at a specified position.

```cpp
vectorName.erase(iterator);
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
auto it = myVector.begin() + 2;
myVector.erase(it);
std::cout << myVector[2]; // Outputs 4
```

## Size and Capacity

The size of a vector is the number of elements it contains. The capacity of a vector is the number of elements it can hold without reallocating memory.

### 1. Using the size() Function

The size() function returns the number of elements in the vector.

```cpp
vectorName.size();
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
std::cout << myVector.size(); // Outputs 5
```

### 2. Using the capacity() Function

The capacity() function returns the number of elements the vector can hold without reallocating memory.

```cpp
vectorName.capacity();
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
std::cout << myVector.capacity(); // Outputs 5
```

### 3. Using the reserve() Function

The reserve() function reserves memory for a specified number of elements in the vector.

```cpp
vectorName.reserve(numberOfElements);
```

For example:

```cpp
std::vector<int> myVector;
myVector.reserve(10);
std::cout << myVector.capacity(); // Outputs 10
```

## Iterators

Iterators are used to traverse the elements of a vector.

### 1. Using the begin() Function

The begin() function returns an iterator to the first element of the vector.

```cpp
vectorName.begin();
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
auto it = myVector.begin();
std::cout << *it; // Outputs 1
```

### 2. Using the end() Function

The end() function returns an iterator to the element following the last element of the vector.

```cpp
vectorName.end();
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
auto it = myVector.end() - 1;
std::cout << *it; // Outputs 5
```

### 3. Using the rbegin() Function

The rbegin() function returns a reverse iterator to the last element of the vector.

```cpp
vectorName.rbegin();
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
auto it = myVector.rbegin();
std::cout << *it; // Outputs 5
```

### 4. Using the rend() Function

The rend() function returns a reverse iterator to the element preceding the first element of the vector.

```cpp
vectorName.rend();
```

For example:

```cpp
std::vector<int> myVector = {1, 2, 3, 4, 5};
auto it = myVector.rend() - 1;
std::cout << *it; // Outputs 1
```

## Sorting

The sort() function is used to sort the elements of a vector in ascending order.

```cpp
std::sort(vectorName.begin(), vectorName.end());
```

For example:

```cpp
std::vector<int> myVector = {5, 4, 3, 2, 1};
std::sort(myVector.begin(), myVector.end());
for (auto i : myVector)
    std::cout << i << " "; // Outputs 1 2 3 4 5
```

## Conclusion

Vectors are a powerful data structure in C++ that can be used to store and manipulate collections of elements. With the functions and methods provided by the STL, vectors can be easily initialized, accessed, modified, and sorted.