# Homework 9

## Learning Outcomes

- MSTs and Union-Find
- MVC
- Iterator

Based on this existing assignment in Java:

This assignment involves animating the construction of a minimum spanning tree to connect BART stations using train tracks.

The learning outcomes are:

- building minimum spanning trees with Kruskal's Algorithm
- implementing the Iterator interface
- detecting and reporting risky concurrency
- analyzing dataset choices with regards to ethics, privacy, and social bias

Recommended resources:

(Actual resources are omitted here because they should be updated and also they're Java-specific)

## A note about BART

We love BART and public transportation, which is why it is the theme of this assignment. But, as we are doing an assignment about "efficient" BART tracks, we must also acknowledge the racist history of those BART tracks when they were built in Oakland.

Here are two articles about the location of the West Oakland BART, which was chosen to disrupt vibrant Black communities: [OaklandVoices](https://oaklandvoices.us/2024/08/05/talk-of-the-town-imagine-west-oakland-before-bart-post-office/#:~:text=In%20the%201950s%20and%201960s%2C%20the%20various,the%20Acorn%20towers%20and%20other%20housing%20projects.) and [TheMetropole](https://themetropole.blog/2024/09/12/bart-disconnects-the-san-francisco-bay-area/#:~:text=BART's%20plans%20especially%20impacted%20West,around%20to%20reap%20these%20benefits.)

As you can see, it is important for us to consider multiple stakeholders when deciding where to build public infrastructure. Please feel free to contribute to this discussion further on Piazza.

## Setup

Accept the assignment from:

Clone it, and set up checkstyle as usual. This assignment uses the Maven build system instead of the Gradle build system, but that should not affect you. See how I started up:

(Video)

If you run into any problems, please post to Piazza with the details. 

If you get a warning about "Timeout while waiting for app reactivation," replace 17.0.2 where it appears in pom.xml with 21.0.1. (This is updating the version of JavaFx.)

As always, you should commit often (at least once per milestone) and regularly push to github.

The main() method is in StationGraphics. When you run the program, you should see this visualization of the station locations:

![image](https://github.com/user-attachments/assets/5d3360ff-8ea5-4954-acad-bc40ce1ac98c)

Note that you can get information about a station by hovering over it:

![image](https://github.com/user-attachments/assets/8477db36-7246-4f4f-91ce-86aa6811f46c)

## Milestone 1: Build and Display Graph

Complete the method makeGraph() in StationMap. It reads in stations from a file and builds a graph with a node for every station. Note that there is a constant NUM_STATIONS that you can modify, which may be helpful for debugging.

You need to complete this method by adding edges connecting each pair of nodes. The weight of the edge should be the distance in miles between their stations. Use the provided helper method, distanceInMiles(). Because the edges are undirected, you should add only one edge between each pair of nodes. Do not make an edge between a node and itself.

After completing the milestone, you should see this when you run the program with a value of 5 for NUM_STATIONS:

![image](https://github.com/user-attachments/assets/c5a95aa1-286b-4179-b4e2-f4f59a687ddd)

## Milestone 2: Build and Display the Minimum Spanning Tree

You will need to change this part of Graph.java:

```
/**
 * Returns an iterator over the edges of a Minimum Spanning Tree of
 * this graph in the order they are added by Kruskal's Algorithm.
 *
 * @return an iterator over the edges of this graph's MST
 */
public Iterator<Edge<T>> getKruskalIterator() {
    return new KruskalIterator<>(this);
}

private static class KruskalIterator<T> implements Iterator<Edge<T>> {
    KruskalIterator(Graph<T> graph) {
    }

    @Override
    public boolean hasNext() {
        return false;
    }

    @Override
    public Edge<T> next() {
        throw new NoSuchElementException();
    }
}
```

Specifically, you will need to replace the stub implementation of the class KruskalIterator<T> with an implementation that provides the edges selected by Kruskal's Algorithm. You must use a PriorityQueue<Edge>. You do not need to write tests.

I suggest pre-computing the first edge in the constructor and storing it in an instance variable so it is available (or null) when hasNext() or next() is called. Similarly, before returning the value in hasNext(), compute and store the next edge.

You should throw ConcurrentModificationException if, after the iterator is created, (1) the outer graph is modified and (2) hasNext() or next() is called.

Once you have completed this part, when you run the program, the MST of the graph will be displayed. Here is what a graph of 5 stations should look like:

![image](https://github.com/user-attachments/assets/ed8300e8-cc70-4a89-a74f-6d4d6cee8482)

The output should be: The minimum spanning tree has 4 edges and is 70 miles long. It is possible you will get a value slightly different from 70 miles due to rounding.

For the final test of your code, set NUM_STATIONS in StationMap to -1. Record the output sentence in Summary.md.

You may want to modify the value of the constant PAUSE_BETWEEN_EDGE_HIGHLIGHTING_MS in Controller to make the updates faster or slower.

## Optional Milestones

If you want, you can:

- add other "stations"
- improve the GUI
- load information cities or transit locations from other parts of the world (which would require changing at least the constants MIN_LATITUDE and MAX_LATITUDE in MapGraphics)
- add [path compression](https://en.wikipedia.org/wiki/Disjoint-set_data_structure) to the union-find implementation

Optional milestones should be made in a separate branch. One place you can learn about git branching is through the first two lessons in the Introduction Sequence at [Learn Git Branching](https://learngitbranching.js.org/):

1. Introduction to Git Commits
2. Branching in Git

Your Gradescope submission should be the original branch without optional milestones.

## Submission

Your final submission must include:

- StationMap.java
- Graph.java
- Summary.md

You may include screenshots of any other changes you made.

## Scoring

- Autograder: 55
 - Checkstyle: 5
 - Instructor unit tests of student code: 50
- Git usage: 5
 - there are commits (at least) at the end of each milestone
 - the final commit to the student branch is the same as the Gradescope submission
 - commit messages are good
 - irrelevant files are not committed
- Manual grading: 18
 - Correctness
   - final output
   - hasNext() implementation
   - next() implementation
 - Style
   - naming
   - code duplication
   - formatting
 - Not attempting to circumvent checkstyle
- Summary.md: 22
