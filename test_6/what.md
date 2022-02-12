## Matrix

[
   
  [0,1,0,0,0,1],  
  [4,0,0,3,2,0],  
]

# markov chains

s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5

Tracing the probabilities of each, we find that

s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14


So, putting that together, and making a common denominator, gives an answer in the form of
[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
[0, 3, 2, 9, 14].
