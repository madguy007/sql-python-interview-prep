1. Sorting strings in Python:
When we apply sort() on a list of strings, Python sorts them lexicographically (dictionary order).  
The ordering is based on characters from left to right, not based on the length of the word.

Example:
Input list:
["flower", "flight", "flow"]

After sorting:
["flight", "flow", "flower"]

Comparison happens character by character:

flight  
flow  
flower  

- first letter → f is same  
- next letter → l is same  
- next letter → i vs o → since i comes before o, "flight" comes first.


2. Why we only compare first and last word:
After sorting, the most similar words come closer and the least similar words move farther apart.

So the first word will have the maximum prefix similarity and the last word will have the minimum prefix similarity.

Example idea:

flower  
flow  
flop  
flat  
flag  

As we move from first to last, the common prefix gradually decreases.

So if the first and last words share a prefix, every word in between must also share that prefix.

Therefore, instead of comparing every word with every other word, we only compare:

first word → words[0]  
last word → words[-1]

The common prefix between these two will be the longest common prefix for the whole list.