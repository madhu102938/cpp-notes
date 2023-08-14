**Q) Checking if N is even or odd**
Of course, we can use our good ol'
```cpp
int isEven(int n)
{
	if (n % 2 == 0)
		return 1;
	else
		return 0;
}
```
but `%` operator is not as fast, so we use this
```cpp
int isEven(int n)
{
	if (n & 1 == 0)
		return 1;
	else
		return 0;
}
```
if a number is even its unit's place will be 0, thus we will get 0 when we perform add operation with 1
*Example*
	lets say n = 6 binary is 110
	`110 & 001` will be `0000`
	if n were 35 binary would be 100011
	`100011 & 000001` will be `000000`

<hr>

**Q) Check if `i`th bit in number `n` is set or not (set if `i`th bit is 1)**
Lets say our N = 1001001 and i = 3
best way to find the answer is 
1001001 & 0001000 answer for this will be non-number if it is **set**, 0 if it is **not** set
```cpp
int isSet(int n, int i)
{
	if (n & (1 << i) == 0)
		return 0;
	else
		return 1;
}
```

<hr>

**Q) set `i`th bit of a number**
Lets say our N = 1001001 and i = 2, then we need to return 1001101
1001001 | 0000100 will be 1001101, thus we need to shift 1 by i bits and perform an OR operation
```cpp
int makeSet(int n, int i)
{
	return n | (1 << i);
}
```

<hr>

**Q) make `i`th bit 0 (`i`th bit can be 1 or 0)**
N = 110110 and i = 2, then we need to return 110010
110110 & 111011 is 110010, 
- thus need to left shift 1 by i 
- negate it 
- then perform AND operation
```cpp
int makeSetZero(int n, int i)
{
	return n & ~(1 << i);
}
```

<hr>

**Q) Remove the last set bit**
N = 110110, we need to return 110100
```cpp
int makeLastSetZero(int n)
{
	return n & (n-1);
}
```

<hr>

**Q) Checking if a number is power of 2**
A power of 2 looks like this `1000000` and number just before it will definitely be `0111111`, so 
AND of those will be 0
```cpp
int isPowerOf2(int n)
{
	return n & (n-1) == 0;
}
```

<hr>

**Q) Count number of set bits in N**
**sol 1**
We are check if each bit is 1 or 0 by performing a AND operation with 1 and right shifting the number by 1 each iteration
```cpp
int noOfSetBits(int n)
{
	int cnt = 0;
	while (n != 0)
	{
		if (n & 1)
			cnt++;
		n = n >> 1;
	}
	return cnt;
}
```
***Time Complexity** - O(Position of MSB in binary)*

**sol2**
We are clearing each set bit from LEFT side
```cpp
int noOfSetBits(int n)
{
	int cnt = 0;
	while (n != 0)
	{
		n = n & (n-1);
		cnt++;
	}
	return cnt;
}
```
***Time Complexity** - O(Number of set bits)*