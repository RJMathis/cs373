# -----------
# Fri,  8 Sep
# -----------

"""
(3n + 1) / 2
3n/2 + 1/2
n + n/2 + 1/2
n + n/2 + 1

b = 10
e = 100
m = 51  mcl(10, 100) = mcl(51, 100)

b = 200
e = 300
m = 151 no claim

Collatz
    workflow
    rubrics
    code

unit testing with Python's unittest
coverage
Collatz optimizations

where exactly in Java is this available and not available
    available     in non-static methods
    not available in     static methods

1 1,000,000 525

what if: 234234 -> 525

cl(5)  -> 6
cl(10) -> 7

mcl(1, 10) -> how much of the cache gets filled?

fill the cache in response to a query, a LAZY cache

fill the cache before any query, an EAGER cache

META cache

instead of caching cycle lengths, we cache max cycle lengths

mcl(   1, 1000)
mcl(1001, 2000)
mcl(2001, 3000)
mcl(3001, 4000)
...

what's mcl(500, 2500)

Questions:
    What two optimizations did we cover in the quiz?
    	halfing the range and bit shifting vs dividing
    What optimization did we cover in lecture?
    	caching
    What is a lazy cache, eager cache, and meta cache?
    	lazy makes the cache on demand ; eager makes the cache during the run;
    	meta makes the cache before a run
    What do each of the caches cache?
    	
    How big should each cache be?
"""
