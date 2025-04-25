# Problem Tracker

## Table of Contents
- [Finding the Number of subarrays that meet a given criteria (eg. holds only -ve numbers).](#001)

---
---
---
---

---
#### 001
`solved`
## Finding the Number of subarrays that meet a given criteria (eg. holds only -ve numbers).


Given an array of integers, you can perform an operation where you select any subarray and flip the signs of all its elements. The goal is to **maximize the total sum** of the array with the **minimum number of such operations**.

To achieve this, the key observation is:
> You only need to flip **contiguous segments of negative numbers** to turn them positive.

So, the task reduces to:
- Count how many **separate negative segments** exist in the array.
- That count is the **minimum number of operations** required to maximize the sum.



```python

def check(n, a):
    l = r =i = count = 0

    while r < n:
        print(a[i])
        # printx(l, r, a[l:r+1], widths=[5])
        while a[r] > 0:
            count += 1
            l = r+1
            r += 1
        r += 1
        i += 1
    return count
```
				
<br><br>
