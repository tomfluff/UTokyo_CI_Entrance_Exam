# 2014 Summer Written Exam

## Question 1
*<u>Note:</u> I don't think I learned this subject before. I am not sure how to solve this question.*

## Question 2
System:
- Processor
- Main memory
- Secondary storage
- Uses logical addresses

### 1
<u>Access time of **main** memory</u> := $T_m$

<u>Access time of **secondary** storage</u> := $T_s$

1. Let us define the size of the data vector (in `KB`): $|V_{data}|=V_{size}$.
2. Let us define the size of the main memory (in `KB`): $|M_{data}|=M_{size}$.

Since page size is `4KB` and since the data is accessed sequencially there will be $TA_{second}$:$V_{size}\cdot \frac{1}{4}$ accesses to the secondary storage. Assuming that each access (read) is done for a whole word (`4B`), then we have:

Total no. of accesses $TA$: $V_{size}\cdot \frac{1024}{4}=V_{size}\cdot \frac{2^{10}}{2^{2}}$

Thus:
1. Page miss ratio = $TA_{second}$
2. Average memory access time = $(T_m\cdot TA + T_s\cdot TA_{second})\cdot \frac{1}{TA}$

With actual values: $T_m=10^2ns$, $T_s=10^6ns$

$(10^2\cdot TA +10^6\cdot TA_{second})\cdot \frac{1}{TA}=10^2 + 10^6\cdot TA_{second}\cdot \frac{1}{TA}=$
$\rightarrow 10^2 + 10^6\cdot TA_{second}\cdot \frac{2^{2}}{2^{10}\cdot V_{size}}=10^2 + 10^6\cdot V_{size}\cdot \frac{1}{2^2} \cdot \frac{2^{2}}{2^{10}\cdot V_{size}}=$
$\rightarrow (10^2 + 10^6\cdot \frac{1}{2^{10}}) ns$

### 2
A program which would give better performance on LRU would be a program which loads the most used static/constant data in the beginning of the execution. This data is accessed frequently. When an instruction is called on new data, it uses the static data as well during the execution. With LRU the static data should not be removed. While in FIFO it will be removed every few iterations of instrucctions (when memory is full).

### 3
One algorithm can be an implementation of a stack using a doudly linked list with pointers to the top and bottom elements. When a page is accessed it will move to the top of the stack. When a page needs replacing we will remove the page from the bottom of the stack and insert the new page to the top of the stack.

## Question 3
### 1
Let filter $H=\begin{bmatrix}
0 & 1 & 0\\
1 &-4 & 1\\
0 & 1 & 0
\end{bmatrix}$
$g(P)=\sum_{n=-1}^{1}\sum_{m=-1}^{1} {f(P_{m,n})\cdot h_{m,n}}=$
$\rightarrow 80+80+250+250+(-4\cdot 150)=60$

### 2
- `(A)` $\rightarrow$ the area of the image (magnitude)
- `(B)` $\rightarrow$ the center of mass of the image (centroid).

|  |Y1|Y2|
|--|--|--|
|$M_{00}$|12|11|
|$M_{10}$|26|28|

### 3
K-NN refers to the algorithm which checks the class assignted to all k nearest points to a given new point and assigns the class of the majority of the points to be the class of the new point. In this methos for $(M_{00},M_{10})=(13,27)$ we will have.
|$k=1$|$k=3$|
|--|--|
|"I"|"C"|
- for $k=1$ we take into account 1 nearest neighbore which is the "I" point at (12,27) based on the definition of eucledian distance. This point is "I" thus the classification is "I" as well.
- for $k=3$ we take the 3 nearest neighbores, (12,27), (12,26), (14,26), with classes "I", "C", "C" respectively. Thus 2/3 have the "C" class and we assign the class "C" to the new point as well.

### 4
The second method proposed uses a reprasentative "fake" point for each cluster of points from a specific class. In this case it is easy to see we would have the `"I"=(10,27)` and `"C"=(12,25)`. Which achieved from $\{P_{class} | \forall_{class}. P_{class}=(\frac{1}{N}\sum_i{x_i},\frac{1}{N}\sum_i{y_i})\}$. For each representative point we will check the nearest distance from the new point to it. In this case it is easy to see the class "C" will be assigned. In our case the check could be defined with the following equasion: $M_{00}-M_{10}+15$ while the result $>0$ the class is `C`, otherwise `I`

### 5
Both algorithms use probablity as their basis and the "chance" of the new point to belong to any class.
- k-NN checks the immidiate environment, and with a good `k` would check proximity to cluster.
- cluster representative gives the average expected point from any cluster and checks the distance to it.
- In a sense because of the definision of $M_{00},M_{10}$ we check similarity on the "area" of the image as well as the center of mass on the `x` axis. 
- This makes the representative have average mass and average center of mass from all points in the cluster.
- When there is little data or the points are spread out the representative might not give the best result. Same as in the case where points of one class are scattarred into several clusters.
- The k-NN will help resolve this issue since it examines the local mean of classes. 
- But with k-NN on situations where the point is on the edge of the "cluster", it might get a false lable in the case where most neighbores are of another class. 
- kNN need no preprocessing, but the classification of a new point takes longer. While representative needs preprocessing of all training data, but classification is quick.

## Question 4
### tf-idf
tf-idf (term frequency inverse document frequency) is used to get a measurement of how "important" a certain word is in a document. The "importance" is defined as $tf/idf(a_{word})=tf_{word | D}(a_{word}) \cdot idf(a_{word})$ where $idf(a_{word})=log(\frac{N}{|\{D\in D_{corpus} | a_{word}\in D\}|})$. This translates to words which are infrequent in relation to the corpus will have more importance, i.e. higher score. Widely used to get weights for ML algorithms.

### ZMP
Zero Moment Point, used in robotics. Can be looked as the point where the center of pressure is located. When walking, the point on the foot where the center of pressure is located. With this concept it is possible to generate a `walk pattern` as a linear equation with relation to ZMP and CoM (Center of Mass). To make a stable body, it needs to have zero velocity **but** also zero momentum (inertia), otherwise it would gain velocity.

### Districuted hash
Distributed hash (DH) is a concept used a lot in networks and communication where a hash data-set is distributed somewhat evenly between the peers. For example circular DH assigns in addition the value of the predecessor and successor to each peer.

### Shortest path problem
This is the problem of finding the shortest path between two points on a given graph (directed or undirected). Given a graph $G$ and vertices $u,v$, the shortest path problem is finding the path $u\rightarrow v$ such that there is no shorter path from $u$ to $v$. The graph can be weighted or unweighted and several algorithms deal with this problem, such as the Dijkstra algorithm.

### Bayesian networks
This concept relates to Machine Learning and is used to compute uncertainties by using the concept of probability. It is represented by a directed asyclic graph. The Baise therom of probablity is used to generate these networks, $P(A|B)= \frac{P(A\cup B)}{P(B)}$ as well as $P(B|A)=\frac{P(A|B)\cdot P(B)}{P(A)}$.

### Carry look ahead
In logic circuets, the carry look ahead adder (CLA) circuet acts faster than a full adder. This is achieved by that it predicts the **carry**. Thus instead of waiting for the sum to be calculated the carry can be predicted prior to that. This allows the result of the sum to be present instantly without waiting for the propegation of the carry.

### Closure
A closure is a concept in programming languages, where functions which were created have access to the local scope in which they were created. A closure closes over the free variables from their environment.

### Finite automaton
Finite automaton (FA) or Finite State Machine, this describes an automaton with a finite set of states. Divided into two categories, with output and without output. FA is the simplest model of computation, and it has a very limited memory. One example of an FA without output is a deterministic finite automaton (DFA).