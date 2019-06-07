import numpy as np
import pomegranate.distributions as dist


from pprint import pprint


if __name__ == "__main__":
    a = dist.DiscreteDistribution({'a': 0.5, 'b': 0.5})
    b = dist.DiscreteDistribution({'a': 0.2, 'b': 0.8})
    c = dist.ConditionalProbabilityTable([['a', 'a', 'a', 0.4],
                                                     ['a', 'a', 'b', 0.6],
                                                     ['a', 'b', 'a', 0.5],
                                                     ['a', 'b', 'b', 0.5],
                                                     ['b', 'a', 'a', 0.01],
                                                     ['b', 'a', 'b', 0.99],
                                                     ['b', 'b', 'a', 0.85],
                                                     ['b', 'b', 'b', 0.15],
                                                     ], [a, b])

    print(c.marginal({a}))
    # print(c.joint())