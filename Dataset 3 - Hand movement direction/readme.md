# BCI-IV

Brain Computer Interfaces has been the focus of my neural network obsession for the past few weeks and I've been trying out different algorithms. This repo is the implementation of many of these for the [BCI Competition Dataset](http://www.bbci.de/competition/iv/)  <br>
I know, I know it's a really old dataset (2008, yikes). <br>

However, as a beginner, these datasets are well processed and have very little artefacts making it easier to focus on the implementation of feep learning models. Additionally, it has been long enough since the competition, that I can 
- Look at the finalists' codes and try to improve on them
- Try newer models and algorithms to see how they compare against those from a decade ago

________________________________________________

This is the implementation of The third Dataset that classifies Hand Movement direction from EEG and MEG signals (Electro- and Magneto-encephalography)

A few key concepts I've exploited here are :
- EEG characteristics are more prominent when they are decomposed into their respective frequency bands (Next step :  Wavelets)
- CNNs are indeed ideal for signals as well, especially non-stationary signals as they extract features that aren't simple or linear patterns. Additionally, patterns in the frequency I suspect help toward the feature extraction
- Residual Networks work great for time series data since past input is passed forward.


I've expanded on all these further in the notebooks.<br>

I'll keep posting updates as and when I try different models (WAVELETS)<br>
Contact me for suggestions!
