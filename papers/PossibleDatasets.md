# Different Possible Datasets
I just found these by googling some stuff

1. [clustering basic benchmark](http://cs.joensuu.fi/sipu/datasets/) This is just a standard set of benchmarks.
There are a lot of standard clusters. I don't know if there are enough clusters for Hausdorrff. It may be possible
that extremely high dimension just euclidean is slow enough. Worm dataset seems interesting and will probably
see significant change due to the algorithm. 

2. One interesting thing that I had not thought of is using MNIST dataset.
This is set of like 60,000 handwritten images. We could use Hausdorff to compute similarity, and then cluster.
This would effectively just solve MNIST and we could check accuracy. [Brief google search found maybe this paper doing similar thing](https://www.irjet.net/archives/V7/i4/IRJET-V7I416.pdf)
The images are pretty small (28x28), so maybe it is less effective I don't know. But there are most certainly 
image benchmark datasets that are out there that we could use. 

