
## `std::queue` Container

`std::queue` is a container in C++ that stores elements in a first-in, first-out (FIFO) order. It provides constant time complexity for insertion and deletion at the back and front of the queue, respectively, but linear time complexity for accessing elements at other positions.

### Declaration

```cpp
std::queue<type> myQueue;
```

### Initialization

```cpp
std::queue<int> myQueue;
```

### Insertion

```cpp
myQueue.push(value);
```

### Deletion

```cpp
myQueue.pop();
```

### Size

```cpp
myQueue.size();
```

### Accessing Elements

```cpp
myQueue.front();
myQueue.back();
```

### Clearing the Queue

```cpp
while (!myQueue.empty())
{
    myQueue.pop();
}
```

### Checking if the Queue is Empty

```cpp
myQueue.empty();
```

### Comparison

```cpp
myQueue1 == myQueue2;
myQueue1 != myQueue2;
```

### Swap

```cpp
std::swap(myQueue1, myQueue2);
```

### Performance

| Operation | Time Complexity |
|-----------|----------------|
| Insertion | O(1)           |
| Deletion  | O(1)           |
| Access    | O(n)           |
| Search    | O(n)           |

### Notes

- `std::queue` stores elements in a first-in, first-out (FIFO) order.
- `std::queue` provides constant time complexity for insertion and deletion at the back and front of the queue, respectively.
- `std::queue` provides linear time complexity for accessing elements at other positions.
- `std::queue` provides functions for inserting and deleting elements.
- `std::queue` provides functions for clearing the queue and checking if the queue is empty.
- `std::queue` provides functions for accessing the front and back elements.
- `std::queue` provides functions for comparing queues and swapping queues.

I hope you find this cheat sheet helpful! Let me know if you have any further questions.