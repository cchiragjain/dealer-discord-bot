# Sources used

* **Visuals** - [Essence of linear algebra by 3b1b](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
* **Theory** - No bullshit guide to linear algebra - Ivan Savov
* **Code** - Jason Brownlee - Basics for Linear Algebra for Machine Learning - Discover the Mathematical Language of Data in Python

[toc]

# Why?

For 2-D and 3-D data we can plot the data points on simple line graphs and draw a line or a plane b/w them but to understand/visualise higher dimensions we can use linear algebra tools to simplify the data & help visualise it.

<img src="./Linear Algebra.assets\image-20210501211152422.png" alt="image-20210501211152422" style="zoom: 67%;" />

# Basic Terminology 


$$
R -> Set\ of\ all\ real\ numbers\\
R^2 -> Set\ of\ all\ ordered\ 2−tuples\\
\{(x_1,x_2 )  | x_1,x_2  ϵ R\}
\\
R^n -> Set\ of\ all\ ordered\ n-tuples\\
\{(x_1,x_2,…,x_n )  | x_1,x_2,…,x_n  ϵ R\}
$$



# Vectors in R^n^

* Ordered list of n-real numbers.

* ![image-20210501212411292](.\Linear Algebra.assets\image-20210501212411292.png)

## Linear Combinations

* For vectors $v_1,v_2,\cdots,v_n\epsilon R$
  * $c_1v_1+c_2v_2+\cdots+c_nv_n$
  * Represents the linear combination



## Span

* The set of all such linear combinations is called the span.
  * For ex. $a=\begin{bmatrix}1\\2\end{bmatrix},b=\begin{bmatrix}0\\3\end{bmatrix} Span(a,b) = R^2$(we can scale this to get our desired vector any way we want).

  * For $a=\begin{bmatrix}2\\2\end{bmatrix},b=\begin{bmatrix}-2\\-2\end{bmatrix}$ the span will be:

    ![image-20210502171611442](./Linear Algebra.assets/image-20210502171611442.png?lastModify=1619956366) 

## Linear Independence

The set of vectors $v_1,v_2,...,v_n$ is linearly independent only if the solution to the equation
$$
\alpha_1.\vec{v}_1+\alpha_2.\vec{v}_2+\cdots+\alpha_n.\vec{v}_n = \vec{0}
\\ is \ \alpha_i=0
\\ for\ all\ i
$$

# Matrix vector product

* [Refer this for visuals](https://youtu.be/kYB8IZa5AuE?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)

* For any matrix vector product ==$A.\vec{v}$ it is just a linear transformation.==

  * Tells us where the vector $\vec{v}$ will land after getting multiplied by matrix A.

    ![](Linear Algebra.assets/matrix-vector product (1).gif)

* In the eqn. $A.\vec{v}=\vec{x}$

  * A is the transformation which we apply
  * $\vec{v}$ is the vector which after getting transformed by A lands on $\vec{x}$

* Any vector $\begin{bmatrix}x\\y\end{bmatrix}$ can be reprensented as

  * $\begin{pmatrix}x\\y\end{pmatrix} = x\begin{pmatrix}1\\0\end{pmatrix}+y\begin{pmatrix}0\\1\end{pmatrix}  $

  * where$\begin{pmatrix}1\\0\end{pmatrix},\begin{pmatrix}0\\1\end{pmatrix}$ are the standard basis vectors $\hat{i}  ,\hat{j}$

  * By knowing the position of the $\begin{pmatrix}1\\0\end{pmatrix} $ & $\begin{pmatrix}0\\1\end{pmatrix} $ we can get the value of any vector $\begin{pmatrix}x\\y\end{pmatrix} $ after multiplication by a matrix $A=\begin{bmatrix}a&b\\c&d\end{bmatrix} $ by:
    $$
    x\begin{pmatrix}a\\c\end{pmatrix} + y\begin{pmatrix}b\\d\end{pmatrix} = \begin{bmatrix}ax&by\\cx&dy\end{bmatrix}
    $$

  * ![image-20210503163243444](Linear Algebra.assets/image-20210503163243444.png)



# Inverse of a Matrix

* **The inverse matrix of a matrix is the transformation we apply to the vector $\vec{x}$ in order to get back to the original vector $\vec{v}$ from which we started.**

  ![](Linear Algebra.assets/inverse transformations.gif)

* The inverse does not exist if $det(A) = 0$

  * Since determinant simply means the area covered by the transformation. If the area/determinant is zero -
    * The transformation squishes space into a smaller dimension
    
      ![](Linear Algebra.assets/determinant=0 case.gif)
    
    * There is no matrix/function that can undo such a thing
    
    * Therefore no inverse exists
  
  
  
  ![](Linear Algebra.assets/transformations.gif)
  
  

# Dot Product

* Dot product is the ==measure of how much the vectors move in the same direction/ how similar they are to each other.==
  $$
  \vec{a}.\vec{b}=\begin{pmatrix}a_1\\a_2\\\vdots\\a_n\end{pmatrix}.\begin{pmatrix}b_1\\b_2\\\vdots\\b_n\end{pmatrix}=a_1.b_1+a_2.b_2+\cdots+a_n.b_n
  \\
  OR\\
  \vec{a}.\vec{b}=|\vec{a}||\vec{b}|cos\theta
  $$

  * For ex. when $\theta=90^{\circ}\ , \vec{a}.\vec{b}=0$ (since there is no projection ($\vec{a}.cos(90)=0) on\ \vec{b}$ now)

* [Refer this for intuition](https://youtu.be/tdwFdzVqito)

# Linear Transformations

* [Refer This](https://youtu.be/XkY2DOUCWMU?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)

# Vector Spaces

A vector space V consists of a **set of vectors and all the possible linear combinations** of such vectors.

## Properties

* **Vector spaces are closed under addition**: for all vectors in that space, the sum of two vectors is also a vector in that vector space. $\forall\ \vec{v_1},\vec{v_2}\ \epsilon\ V, \vec{v_1}+\vec{v_2}\ \epsilon\ V$
* **Vector spaces are** **closed under scalar multiplication** : $\forall\ \alpha\ \epsilon\ R\ \&\ \vec{v}\ \epsilon\ V,\ \alpha\vec{v}\ \epsilon\ V$

## Basis of a Vector Space

* **Minimum set of linear independent vectors that spans the entire space** and can be used to create any vector in that space.
  * For ex, Let $v_1,v_2,v_3$ be 3 vectors in a vector space V such that $v_3= v_1+v_2$
    * This will not form a basis since they are not linearly independent $v_3=v_1+v_2

## Dimension of a Vector Space

- **Number of elements in the basis** of a vector space.

- - Dimension of a null space - **NULLITY**
  - Dimension of column/row space - **RANK**

## Fundamental Matrix Spaces

- The **column space C(M)** is the span of the columns of the matrix . 

- - **Consists of - all possible output vectors the matrix can produce when      multiplied by a vector from the right.**

* The **null space N(M)** of a matrix $M\ \epsilon\ R^{m*n}$ **consists of all vectors the** **matrix** **M** **sends to the zero vector** ( see matrix vector product )
  $$
  N(M) = \{\vec{v}\ \epsilon\ R^n\ |\ M\vec{v}=\vec{0}\}
  $$
  
  * This can be     used to solve linear system of homogenous equations.
  
  - <mark>**Also if a set of vectors are linearly independent then N(A) = $\vec{0}$**</mark>

# Norms

* The length of a vector is a non-negative number that describes **the extent of the vector in space** to as the **vector norm.**

