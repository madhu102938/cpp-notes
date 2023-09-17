**Sub-sequence** - A contiguous or non - contiguous sequence, which follows order
### Printing all sub-sequences
```cpp
#include <iostream>
#include <vector>

int allSubsequences(std::vector<int> &v, std::vector<int> &temp, int index = 0)
{
    if(index >= v.size())
    {
        for(auto i : temp)
            std::cout << i << " ";
        std::cout << std::endl;
        return 0;
    }
    temp.push_back(v[index]); // include the element
    allSubsequences(v, temp, index + 1);
    temp.pop_back(); // exclude the element
    allSubsequences(v, temp, index + 1);
}

int main()
{
    std::vector<int> v;
    int N;
    std::cout << "Enter the number of elements: ";
    std::cin >> N;
    std::vector<int> temp;
    std::cout << "Enter the elements: ";
    for (int i = 0; i < N; i++)
    {
        int temp;
        std::cin >> temp;
        v.push_back(temp);
    }
    std::cout << allSubsequences(v, temp);
    return 0;
}
```
<hr>
Tree diagram for `vector = {3, 2, 1}`
[Imgur](https://imgur.com/MiCXoqD)
<hr>
We can also do it in reverse by excluding the element first and then including it later.
***Time complexity** - O($n*2^n$)*
- For each index, either we pick or don't pick, so it is $2^n$ and we print them with for loop, so an additional $n$, upon combining we get $n*2^n$
***Space complexity** - O($n$)*
- space complexity is the depth of the tree, thus at maximum only $n$ function calls wait in the stack.

### Find all subsequences which add up to target
```cpp
#include <iostream>
#include <vector>

int sumSubsequences(std::vector<int> &v, std::vector<int> &temp, int sum, int index = 0, int sumTemp = 0)
{
    if(index == v.size())
    {
        if(sumTemp == sum)
        {
            for(auto i : temp)
                std::cout << i << " ";
            std::cout << std::endl;
            return 0;
        }
        return 0;
    }
    temp.push_back(v[index]); // include
    sumTemp += v[index]; 
    sumSubsequences(v, temp, sum, index + 1, sumTemp);
    sumTemp -= v[index]; // exclude
    temp.pop_back();
    sumSubsequences(v, temp, sum, index + 1, sumTemp);
}

int main()
{
    std::vector<int> v;
    int N;
    std::cout << "Enter the number of elements: ";
    std::cin >> N;
    std::vector<int> temp;
    std::cout << "Enter the elements: ";
    for (int i = 0; i < N; i++)
    {
        int temp;
        std::cin >> temp;
        v.push_back(temp);
    }
    int sum;
    std::cout << "Enter the sum: ";
    std::cin >> sum;
    sumSubsequences(v, temp, sum);
    return 0;
}
```
We are using pick - no pick approach for this
- incase we are picking it, we are increasing the index and going to the next element
- incase we are not picking it, we are increasing the index by one, then we think about either picking up the next element or not.


**But how to print one answer to the target, instead of printing of all answers?**
we have to use something like this : 
```cpp
auto func()
{
	if(base case)
		return true;
	else
		return false;
	
	if (func() == true) //first recursion call
		return true;
	if (func() == true) //second recursion call
		return true;
	return false;
}
```

```cpp
#include <iostream>
#include <vector>

bool sumSubsequences(std::vector<int> &v, std::vector<int> &temp, int sum, int index = 0, int sumTemp = 0)
{
    if(index == v.size())
    {
        if(sumTemp == sum)
        {
            for(auto i : temp)
                std::cout << i << " ";
            std::cout << std::endl;
            return true;
        }
        return false;
    }
    temp.push_back(v[index]); // include
    sumTemp += v[index]; 
    if(sumSubsequences(v, temp, sum, index + 1, sumTemp)) return true;
    sumTemp -= v[index]; // exclude
    temp.pop_back();
    if(sumSubsequences(v, temp, sum, index + 1, sumTemp)) return true;
    return false;
}

int main()
{
    std::vector<int> v;
    int N;
    std::cout << "Enter the number of elements: ";
    std::cin >> N;
    std::vector<int> temp;
    std::cout << "Enter the elements: ";
    for (int i = 0; i < N; i++)
    {
        int temp;
        std::cin >> temp;
        v.push_back(temp);
    }
    int sum;
    std::cout << "Enter the sum: ";
    std::cin >> sum;
    sumSubsequences(v, temp, sum);
    return 0;
}
```


**how to print just the number of sub-sequences instead of the actual sub-sequences**
```cpp
auto func()
{
	if(base case)
		return 1;
	else
		return 0;
	left = func();
	right = func();
	return left + right;
}
```

```cpp
#include <iostream>
#include <vector>

int sumSubsequences(std::vector<int> &v, int sum, int index = 0, int sumTemp = 0)
{
    if (index >= v.size())
    {
        if (sumTemp == sum)
            return 1;
        else
            return 0;
    }
    sumTemp += v[index];
    int left = sumSubsequences(v, sum, index + 1, sumTemp);
    sumTemp -= v[index];
    int right = sumSubsequences(v, sum, index + 1, sumTemp);
    return left + right;
}

int main()
{
    std::vector<int> v;
    int N;
    std::cout << "Enter the number of elements: ";
    std::cin >> N;
    std::cout << "Enter the elements: ";
    for (int i = 0; i < N; i++)
    {
        int temporary;
        std::cin >> temporary;
        v.push_back(temporary);
    }
    int sum;
    std::cout << "Enter the sum: ";
    std::cin >> sum;
    std::cout << sumSubsequences(v, sum);
    return 0;
}
```