
### 001

There were a fair number of specifics I hadn't seen before (stringIO/Timestamp/multi-indexing) and it took me a while but by going through and looking things up and making some small modifications like going to regular DF from MI Series I solved the exercises.

I would not have been able to write all of this from scratch without looking things up or with a very stringent time-constraint though, but it was the first-pass and I will get more familiar/speed up.

*TODO: Last Ex1*

### 002

I found this substantially less challening, though there were a bunch of little tricks in there I didn't know like being able to do .pct_change() or .cumprod() rather than having to write loops (and .rolling()), which are all very useful.

The vol-targeting solution generally came naturally as a way to get portfolio weights ("equal risk contribution") but I hadn't seen it done in a rolling way before.

It would be interesting to do it with autocorrelation rather than sum over a window and to implement some sort of proper portfolio rebalancing logic so could it track associated positions and get portfolio return.

### Qs

- Will I be allowed to use documentation / assistance tools / look things up?
- How much time can I expect?

### Thoughts

- I need to practice - the longer I have to prepare myself and get to know these tools, the better - but I will make it work 100% either way.
