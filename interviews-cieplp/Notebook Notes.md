
### 001

There were a fair number of specifics I hadn't seen before (stringIO/Timestamp/multi-indexing) and it took me a while but by going through and looking things up I was able to understand and making some small modifications (like going to regular DF from MI Series) to solve the exercises.

I definitely would not have been able to write all of this from scratch without looking things up or with a very stringent time-constraint, though this is first-pass and I will get more familiar/speed up.

*TODO: Last Ex From 001*

### 002

I found this substantially less challening, though there were a bunch of little tricks in there I didn't know, like being able to do .pct_change() or .cumprod() rather than having to write loops, .rolling(), which are all useful.

Also the vol-targeting solution generally came naturally as a way to get portfolio weights ("equal risk contribution") but I hadn't seen it done in a rolling way before, just a static weight based on historical vol

Would be interesting to do it with autocorrelation rather than sum over a window and to implement some sort of proper portfolio rebalancing logic so could track associate positions and get portfolio return.

### Qs

- Will I be allowed to use documentation / assistance tools / look things up?
- What timeframe can I expect?

### Current Thoughts

- I definitely need to practice pandas a bunch as and get really comfortable with it as a first order of business, the syntax is somewhat convoluted.
- I think my first impression is that the longer I have to prepare myself and get to know these tools, the better - though I'll make it work either way.
- I am also really unwell and feverish now, so hopefully a swift return to health will assist.
