
## `std::priority_queue` Container

`std::priority_queue` is a container in C++ that stores elements in a priority order. It provides constant time complexity for insertion and deletion of the highest priority element, but linear time complexity for accessing elements at other positions.

### Declaration

```cpp
std::priority_queue<type> myPriorityQueue;
```

### Initialization

```cpp
std::priority_queue<int> myPriorityQueue;
```

### Insertion

```cpp
myPriorityQueue.push(value);
```

### Deletion

```cpp
myPriorityQueue.pop();
```

### Size

```cpp
myPriorityQueue.size();
```

### Accessing Elements

```cpp
myPriorityQueue.top();
```

### Clearing the Priority Queue

```cpp
while (!myPriorityQueue.empty())
{
    myPriorityQueue.pop();
}
```

### Checking if the Priority Queue is Empty

```cpp
myPriorityQueue.empty();
```

### Comparison

```cpp
myPriorityQueue1 == myPriorityQueue2;
myPriorityQueue1 != myPriorityQueue2;
```

### Swap

```cpp
std::swap(myPriorityQueue1, myPriorityQueue2);
```

### Performance

| Operation | Time Complexity |
|-----------|----------------|
| Insertion | O(log n)       |
| Deletion  | O(log n)       |
| Access    | O(n)           |
| Search    | O(n)           |

### Notes

- `std::priority_queue` stores elements in a priority order.
- `std::priority_queue` provides constant time complexity for insertion and deletion of the highest priority element.
- `std::priority_queue` provides linear time complexity for accessing elements at other positions.
- `std::priority_queue` provides functions for inserting and deleting elements.
- `std::priority_queue` provides functions for clearing the priority queue and checking if the priority queue is empty.
- `std::priority_queue` provides functions for accessing the highest priority element.
- `std::priority_queue` provides functions for comparing priority queues and swapping priority queues.

I hope you find this cheat sheet helpful! Let me know if you have any further questions.