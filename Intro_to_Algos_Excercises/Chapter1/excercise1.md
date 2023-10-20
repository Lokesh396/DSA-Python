## Excercise 1

###### 1.1-1 Give a real-world example that requires sorting or a real-world example that requires computing a convex hull ?

In realtime sorting was used in contacts in mobile and file managers in computers and mobile phones.

###### 1.1-2 Other than speed, what other measures of efficiency might use in a real-world setting ?
- Space
- Relaibility

###### 1.1-3 Select a data structure that you have seen previously, and discuss its strengths and weakness?

Let's discuss about the *strength* and *weakness* of **list**.

###### Strengths:
1. Random accesses : We can access any element of an array using the index value and the base address of the array. Every element can be accessed in O(1) time (assuming whole array is in the main memory)
2. Serial allocation : Usually, the arrays occupy consecutive memory locations for its elements. So, we can delete the array in one step by deallocating the whole memory area at once. Another advantage of serial allocation is, if the array is too big, accessing consecutive elements takes fewer disk seeks than say in linked lists(where elements could be scattered across the memory).
3. Faster Search : Algorithms like binary search and interpolated search can only be applied on SORTED arrays.

 ###### Limitations:
1. Deleting/Inserting random elements : When we delete a random element in an array we may need to shift all elements ahead of it left by one place - worst case O(n). Same is the case when we are maintaining a sorted array and want to insert a random element.
2. Unsorted Array is not good for searching when we have very large number of elements - as we need to perform Linear search - O(n) time.
3. Static nature :- In most languages, array are statically allocated. So, we may end of reserving extra space then needed or we may not be able to add more elements as needed.

###### 1.1-4 How are the travelling-salesman problem given above similar? How they are different?

They are similar, because each of then has to walk a graph and find a path in them.

The difference is the constraint on the solution. The shortest-path requires just a path between two points, while the traveling salesman requires a path between more points that returns to the first point.

###### 1.1-5 Come up with a real-world problem in which only the best solution will do. Then come up with one in which a solution that is "approximately" the best is good enough.

Let's take Instagram, where they have millions of users, if a person want to search a user if they use insertion sort(users was not stored in sorted order) to search for that, it will take many years to search.So, it is better to use any algorithm which is fast like quick sort or merge sort which will take less time
compared to insertion sort.

If we take contacts in our example, it is stored in sorted order. If we want to search a user from contacts, even if they are not in sorted order, as the contacts is less. It will take less time for searching.