### Word Ladder I
**1Q)** A **transformation sequence** from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that:

- Every adjacent pair of words differs by a single letter.
- Every `si` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.
- `sk == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return _the **number of words** in the **shortest transformation sequence** from_ `beginWord` _to_ `endWord`_, or_ `0` _if no such sequence exists._

```cpp
int wordLadderLength(string startWord, string targetWord, vector<string> &wordList)
{
// Creating a queue ds of type {word,transitions to reach ‘word’}.
	queue<pair<string, int>> q;

	// BFS traversal with pushing values in queue 
	// when after a transformation, a word is found in wordList.
	q.push({startWord, 1});

	// Push all values of wordList into a set
	// to make deletion from it easier and in less time complexity.
	unordered_set<string> st(wordList.begin(), wordList.end());
	st.erase(startWord);
	while (!q.empty())
	{
		string word = q.front().first;
		int steps = q.front().second;
		q.pop();

		// we return the steps as soon as
		// the first occurence of targetWord is found.
		if (word == targetWord)
			return steps;

		for (int i = 0; i < word.size(); i++)
		{
			// Now, replace each character of ‘word’ with char
			// from a-z then check if ‘word’ exists in wordList.
			char original = word[i];
			for (char ch = 'a'; ch <= 'z'; ch++)
			{
				word[i] = ch;
				// check if it exists in the set and push it in the queue.
				if (st.find(word) != st.end())
				{
					st.erase(word);
					q.push({word, steps + 1});
				}
			}
			word[i] = original;
		}
	}
	// If there is no transformation sequence possible
	return 0;
}
```

<hr>

### Word ladder II
**2Q)** A **transformation sequence** from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that:

- Every adjacent pair of words differs by a single letter.
- Every `si` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.
- `sk == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return _all the **shortest transformation sequences** from_ `beginWord` _to_ `endWord`_, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words_ `[beginWord, s1, s2, ..., sk]`.

```cpp
vector<vector<string>> findSequences(string beginWord, string endWord, 
									 vector<string> &wordList)
{
	// Push all values of wordList into a set
	// to make deletion from it easier and in less time complexity.
	unordered_set<string> st(wordList.begin(), wordList.end());
	
	// Creating a queue ds which stores the words in a sequence which is
	// required to reach the targetWord after successive transformations.
	queue<vector<string>> q;

	// BFS traversal with pushing the new formed sequence in queue 
	// when after a transformation, a word is found in wordList.

	q.push({beginWord});

	// A vector defined to store the words being currently used
	// on a level during BFS.
	vector<string> usedOnLevel;
	usedOnLevel.push_back(beginWord);
	int level = 0;
   
	// A vector to store the resultant transformation sequence.
	vector<vector<string>> ans;
	while (!q.empty())
	{
		vector<string> vec = q.front();
		q.pop();

		// Now, erase all words that have been
		// used in the previous levels to transform
		if (vec.size() > level)
		{
			level++;
			for (auto it : usedOnLevel)
			{
				st.erase(it);
			}
		}

		string word = vec.back();

		// store the answers if the end word matches with targetWord.
		if (word == endWord)
		{
			// the first sequence where we reached end
			if (ans.size() == 0)
			{
				ans.push_back(vec);
			}
			else if (ans[0].size() == vec.size())
			{
				ans.push_back(vec);
			}
		}
		for (int i = 0; i < word.size(); i++)
		{   
			// Now, replace each character of ‘word’ with char
			// from a-z then check if ‘word’ exists in wordList.
			char original = word[i];
			for (char c = 'a'; c <= 'z'; c++)
			{
				word[i] = c;
				if (st.count(word) > 0)
				{ 
					// Check if the word is present in the wordList and
					// push the word along with the new sequence in the queue.
					vec.push_back(word);
					q.push(vec);
					// mark as visited on the level
					usedOnLevel.push_back(word);
					vec.pop_back();
				}
			}
			word[i] = original;
		}
	}
	return ans;
}
```