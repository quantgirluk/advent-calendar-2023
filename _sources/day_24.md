# Day 24 : Normal Distribution

The normal distribution, also known as the Gaussian distribution after German mathematician [Carl Friedrich Gauss](https://en.wikipedia.org/wiki/Carl_Friedrich_Gauss), is probably the most popular probability distribution. It has became ubiquitous in many areas of knowledge and most people recognise its familiar bell-shaped curve. It has support in $(-\infty, \infty)$ and is defined by two parameters. The shape parameter $\mu$ is the mean or expectation of the distribution (and also its median and mode!), while the scale parameter $\sigma$ is its standard deviation.

![](../images/24_Normal.png)

Its probability density function is given by

$$f(x) = \frac{1}{2\sqrt{\pi}} \exp\left\{-\frac{1}{2} \left(\frac{x-\mu}{\sigma}\right)^2 \right\}$$

Its cumulative distribution function is give by

$$F(x) = \frac{1}{2} \left[1 + \hbox{erf}\left(\frac{x-\mu}{\sigma \sqrt{2}} \right)\right],$$

where $\hbox{erf}$ denotes the [error function](https://en.wikipedia.org/wiki/Error_function).

## 🔔 Random Facts 🔔

- It is sometimes informally called a bell curve. However, many other distributions are bell-shaped (such as the Cauchy, Student's _t_, and logistic distributions). 

- About 68% of values drawn from a normal distribution are within one standard deviation _σ_ away from the mean; about 95% of the values lie within two standard deviations; and about 99.7% are within three standard deviations. This popular fact is known as the [68-95-99.7 (empirical) rule](https://en.wikipedia.org/wiki/68%E2%80%9395%E2%80%9399.7_rule), or the _3-sigma rule_.

- The Gaussian distribution belongs to the family of [stable distributions](https://en.wikipedia.org/wiki/Stable_distribution) which are the attractors of sums of independent, identically distributeddistributions whether or not the mean or variance is finite. Except for the Gaussian which is a limiting case, all stable distributions have heavy tails and infinite variance. It is one of the few distributions that are stable and that have probability density functions that can be expressed analytically, the others being the Cauchy distribution and the Lévy distribution.

- In [standardized testing](https://en.wikipedia.org/wiki/Standardized_testing_\(statistics\)), results can be made to have a normal distribution by either selecting the number and difficulty of questions (as in the IQ test) or transforming the raw test scores into output scores by fitting them to the normal distribution. For example, the [SAT](https://en.wikipedia.org/wiki/SAT)'s traditional range of 200–800 is based on a normal distribution with a mean of 500 and a standard deviation of 100.

Today's bonus consists of simulation of a Brownian motion and an Ornstein–Uhlenbeck process. Both processes have marginal densities normally distributed.

![](../images/ou_process_drawn.png)

![](../images/24_Normal_Bonus.png)