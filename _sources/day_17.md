# Day 17 : Generalised Extreme Value

The generalized extreme value (GEV) distribution is a family of continuous probability distributions developed within [extreme value theory](https://en.wikipedia.org/wiki/Extreme_value_theory) to combine the [Gumbel](https://en.wikipedia.org/wiki/Gumbel_distribution), [Fréchet](https://en.wikipedia.org/wiki/Fr%C3%A9chet_distribution) and [Weibull](https://en.wikipedia.org/wiki/Weibull_distribution) families which are also known as type I, II and III Extreme Value Distributions (EVD). It is defined by three parameters: a location parameter $\mu\in\mathbb{R}$, a scale parameter $\sigma>0$, and a shape parameter $\xi\in\mathbb{R}$. The shape parameter defines which distribution the generalised extreme value distribution takes on:

- When $\xi$ is equal to 0, the GEV is equal to EVD Type I ([Gumbel](https://en.wikipedia.org/wiki/Gumbel_distribution)).

- When $\xi$ is greater than 0, the GEV is equal to EVD Type II ([Fréchet](https://en.wikipedia.org/wiki/Fr%C3%A9chet_distribution)).

- When $\xi$ is less than 0, the GEV is equal to EVD Type III ([Weibull](https://en.wikipedia.org/wiki/Weibull_distribution)).

![](../images/17_GeneralisedExtremeValue.png)

The probability density function is given by

$$f(x) = \frac{1}{\sigma} t(x)^{\xi + 1} e^{-t(x)},$$

where

$$t(x) = \begin{cases} \left[ 1 + \xi \left( \frac{x-\mu}{\sigma} \right) \right]^{-\frac{1}{\xi}} & \hbox{if } \xi\neq 0,\\ \exp\left(- \frac{x-\mu}{\sigma} \right) & \hbox{if } \xi=0 \end{cases}.$$

The cumulative distribution function is given by

$$F(x) = e^{-t(x)},$$

where $t(x)$ is defined as above.

## 🔔 Random Facts 🔔

- In some fields of application the generalized extreme value distribution is known as the Fisher–Tippett distribution, after British polymath [Ronald Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher) and English statistician [L. H. C. Tippett](https://en.wikipedia.org/wiki/L._H._C._Tippett) who recognised three different forms of the family. 

- The GEV distribution is widely used in the treatment of "tail risks" in fields ranging from insurance to finance. In the latter case, it has been considered as a means of assessing various financial risks via metrics such as [value at risk](https://en.wikipedia.org/wiki/Value_at_risk) (VaR).

- In [hydrology](https://en.wikipedia.org/wiki/Hydrology) the GEV distribution is applied to extreme events such as annual maximum one-day rainfalls and river discharges. See e.g. the paper "[Quantifying annual occurrence probability of rainfall-induced landslide at a specific slope](https://www.sciencedirect.com/science/article/abs/pii/S0266352X22002245?via%3Dihub)" published in 2022.

- If $X\sim Exponential(1)$, then for any $\mu\in\mathbb{R}, \sigma>0$ the random variable $Y = \mu - \sigma \log X$ follows a GEV distribution with parameters $\mu, \sigma$ and $\xi=0$, i.e. $Y\sim GEV(\mu, \sigma, 0)$.

Today's bonus is a picture of an art piece by an unknown author showing Lisbon, Portugal, during the great [earthquake of 1 November 1755](https://en.wikipedia.org/wiki/1755_Lisbon_earthquake). This copper engraving, made that year, shows the city in ruins and in flames. Tsunamis rush upon the shore, destroying the wharfs. The engraving is also noteworthy in showing highly disturbed water in the harbor, which sank many ships. Passengers in the left foreground show signs of panic. Extreme value theory is used to model the risk of extreme, rare events, such as the [1755 Lisbon earthquake](https://en.wikipedia.org/wiki/1755_Lisbon_earthquake).

<figure>

![](../images/1755_Lisbon_earthquake.jpg)

<figcaption>

Source: Wikipedia Extreme Value Theory

</figcaption>

</figure>
