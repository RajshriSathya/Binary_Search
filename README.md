*What is Binary Search?
Binary Search is an efficient searching algorithm that finds an element by repeatedly dividing the search space into half. It works only on sorted arrays.

*How Binary Search Works?

1.Start with the first (low) and last (high) index.
2.Find the middle index using (low + high) // 2.
3.Compare the middle element with the target.
4.If it matches → element found.
5.If target is smaller → search the left half.
6.If target is larger → search the right half.
7.Repeat until the element is found or the range end.