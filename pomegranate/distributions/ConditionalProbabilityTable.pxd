# ConditionalProbabilityTable.pxd
# Contact: Jacob Schreiber <jmschreiber91@gmail.com>

import numpy
cimport numpy

from .distributions cimport MultivariateDistribution

cdef class ConditionalProbabilityTable(MultivariateDistribution):
	cdef double* values
	cdef double* counts
	cdef double* marginal_counts
	# n is the number of entries in the CPT, k is the cardinality of the variable.
	cdef int n, k
	cdef public int n_columns
	cdef int* idxs
	cdef int* marginal_idxs
	cdef public numpy.ndarray column_idxs
	cdef int* column_idxs_ptr
	cdef public list parents, parameters, dtypes
	cdef public object keymap
	cdef public object marginal_keymap
	# m is the number of parents
	cdef public int m
	cdef void __summarize(self, items, double [:] weights)

