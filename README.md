# Google_Sort
Solving the coding challenge for getting a Job at Google

## The popular software developer, tutor and youtuber Tech with Tim posted a challenge, which will probably get you a job at google. Since I am currently looking for a job
## I chose to solve the problem.

## This is the video I am responding to https://www.youtube.com/shorts/HsaGeSA8dAk

### Problem: You have a list of unsorted integers like so: [2, 7, 3, 8, 1, 4]. You must sort the list like so. [1, 2, 3, 4, 7, 8]. You are only allowed to swap
### adjacent numbers like so [7, 3] -> [3, 7]. Find the algorithm, which sorts the list with the **minimum number of swaps**.

### Tech with Tim gives as a visual hint at the end of the video, which shows bubbles. Thus, all respondents suggest that bubble sort is the solution.
### Bubble sort merely loops through the list and swaps adjacent numbers, if they are not in order. Looping is repeated until the list is sorted. 
### I understand that this will eventually lead to a sorted list, but it is by no means clear why the list is sorted with *minimum number of swaps**. Therefore,
### I developed an algorithm, which arguably guarantees a minimum number of swaps.

### 1. Idea: Identify the final position of list elements in order to minimize the swaps to its final position.

### 2. Idea: This is very difficult for an arbitrary element. However, the smallest element must be at the beginning and the largest element at the end of the list.

### 3. Idea: Move the smallest element with the minimum number of steps to its final position, the beginning of the list. Swap the smallest element 1 with its left neighbor 
### until it lands at the beginning of the list like so: [1, 2, 7, 3, 8, 4]

### 4. Idea: Recognize that this operation does not change the relative ordering of the residual elements of the list [2, 7, 3, 8, 1, 4]. Thus, this operation has no
### impact on the number of steps necessary for ordering the residual elements. At the same time, moving the smallest element to the beginning in this manners is the
### fastest manner to do so. Therefore, it is optimal

### 5. Idea: Remove the first element from the list like so [1] and repeat this algorithm with the residual list [2, 7, 3, 8, 4]
