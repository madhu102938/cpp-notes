Practice questions @01:42:00
Where clause doesnt work
Testing where clause (instead of using having)
Where -> rows, having -> groups
Using all the clauses at once
Truncate / drop
Self join
Union all



-- lec 1 --
Multinomial
Broadcasting
Bigram model based on probability
Neural nets
Smoothing (in count method and nn method) (regularisation)
Proving both models produce same results

-- lec 2 --
Count method -> exponential growth
**Paper - Neural probabilistic language model**
Word embeddings (30 dim)
Torch.unbind
View is efficient
Pytorch internals blogpost
Negative log loss is cross entropy (more efficient)
> Forward pass efficient
> Backward pass efficient
> Numerically well behaved

Mini batches
Finding the proper learning rate 
Learning rate decay
If loss is oscillating too much then, mini batch might be too small


-- lec 3 --
Initialisation problem
- Values of output layer too high
   - We can initialise output weights with low values, and set output bias to be zero
- Values coming out from activations being too high, thus making the gradient zero, thus having a dead neuron
  - we can avoid this by using some other activations (leaky relu)
  - initializing hidden layer weights, biases closer to zero
- basically the std deviation (spread) increases, we need to reset that and make it 1, we can do this by multiplying it with 1/√(neurons in the layer)
  - different activations have different factors, checking kiming_normal
- torch.nn.init.kiming_normal
- but because of recent advances (batch norm, layer norm, skip connections, Adam optimizer) we don't need to worry about this much
**Paper - batch normalisation 2015 Google**
Regularising affect of batch norm
   - postive effect
   - negative effect
Batch norm is normally added after multiplications that is after conv or linear layers
Adding bias to the layer before batch norm is wasteful as mean of that would be zero, thus bias can be left out
Running mean, bias - tracking for training
Momentum of batch norm (pytorch docs of batch norm)

