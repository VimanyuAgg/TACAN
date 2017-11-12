# TACAN 
## (Traffic Aware Clustering in Adhoc Networks)

### Overview: 
Obtaining a hierarchical organization of a network is a well-known and important problem in the field of wired networks. In the case of ad hoc networks , wireless networks in which possibly all nodes can be mobile, partitioning the nodes into groups (clusters) is similarly important. With the advent of multimedia communications, the use of the cluster architecture has peaked like never before and there is a significant emphasis towards the allocation of resources, namely, bandwidth and channel, to support multimedia traffic in an ad hoc environment.

At present the most common clustering approach used in ad hoc networks is size-bounded clustering that restricts the number of nodes in a cluster. The constraint on size bounds the routing load and energy drain on the clusterhead. These clustering algorithms revolve around the assumption that there is uniform traffic throughout the cluster. But with such a vast number of applications, there are cases where the routing load on the clusterhead is high and the whole purpose of having a size-bound cluster gets defeated [1].

In this project, we are implementing an algorithm proposed by [2], which forms a traffic-aware and energy-efficient clustering scheme. It takes into consideration the average traffic pattern between nodes in forming the cluster thereby considering a more realistic measure of routing load on the cluster heads [2].

### REFERENCES
[1] S. Basagni, “Distributed clustering for ad hoc networks.” In Parallel Architectures, Algorithms, and Networks, 1999. (I-SPAN'99) Proceedings. Fourth InternationalSymposium on (pp. 310-315). IEEE. doi: 10.1109/ISPAN.1999.778957

[2] B. S. Tiwana and A. Gupta, “A distributed algorithm for traffic aware clustering in ad hoc networks.” in Services Computing Conference, 2009. APSCC 2009. IEEE Asia-Pacific (pp. 75-80). IEEE. doi: 10.1109/APSCC.2009.5394138

### Deployment Diagram:

![Alt text](https://github.com/VimanyuAgg/TACAN/blob/master/Deployment%20Diagram.png "Deployment Diagram")

### UML Sequence Diagram: Phase 1 Clustering:

![Alt text](https://github.com/VimanyuAgg/TACAN/blob/master/Phase1-sequence_diagram.png "Ph1 Sequence Diagram")
