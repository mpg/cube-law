When chatting with my step-brother about the time it takes to solve [big
Rubik's cubes](https://en.wikipedia.org/wiki/Rubik%27s_Cube#Variations) I
half-jokingly said it would made sense for the growth to be... cubic.

But is it? What does the data say?

## Data sources

1. [wca](https://www.worldcubeassociation.org/results/records?show=mixed)
2. [uwr](https://www.speedsolving.com/wiki/index.php/List_of_Unofficial_World_Records#Big_cubes)

- all = uwr + wca
- big = uwr + wca - (2x2 and 3x3)

- single = best single solve
- ao5 = truncated average of 5, aka "average", aka "avg5"

From `uwr-single` I excluded 16, 19 and 23 because the times just seemed out of
place (16 and 19 are slower that larger cubes).

### Thoughts on data sets

- 2x2 and 3x3 solves are probably over-optimized compared to bigger cubes: 3x3
  because it's the main event, and 2x2 because top solvers 1-look it (that is,
  they plan the entire solve during inspection), so arguably a larger proportion
  of the solve happens during inspection. Hence the `big-*` data sets.
- In the same vein, people probably train more for the sizes with official WCA
  times (that is, up to 7 included), than for the larger sizes.
- Mixing data from different sources (wca+uwr) has obvious issues; OTOH each
  data set on its own is pretty small.
- Average of 5 is probably less noisy (lucky scrambles) than single; OTOH single
  has a few more sizes available.

Overall, my (poorly informed) opinion is that `big-single` is probably the least
bad dataset.

## Data analysis

Since my starting half-joke hypothesis is that t is proportional to n³ I started
just plotting the data points in log-log scale to check if they looked roughly
aligned. They did, so then I wanted to check the slope of the line.

That's when things started being more complicated. You can do the fit in
log-space or on the original data; on `wca-ao5` (the original dataset I used)
these two ways gave significantly different exponents. Also, 2x2 and 3x3 seemed
to be outsiders when fitting the original data. Also, what if the model is
more like t = c + k * n^e? Also, if I do that and exclude 2 and 3, I have barely
more data points that variables to fit, which does not smell good at all.

I collected more data, but don't have the skills to go further in the
statistical analysis.

### Conclusion

1. Stats is hard. (Confidence: high.)
2. The growth seems to be more than cubic. (Confidence: low.)
