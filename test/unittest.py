
import os
import shutil
import numpy as np
from unittest import TestCase, main
from sentsation.text import feature_extraction as fe

class TestSentiScorer(TestCase):
    def setUp(self):
        self.data = ['this is a wonderful day', 'really bad behaviour',
                     'not to complaint', 'good very good']

    def test_transformer_avg(self):
        ssr = fe.SentiScorer(transform_POS=True, dropna=True, synsets_aggregation='avg')
        actual = ssr.transform(self.data)
        expected = np.array([[0.8       , 0.        ],
                            [0.51785714, 0.72321429],
                            [0.        , 0.625     ],
                            [1.48809524, 0.13690476]])
        np.testing.assert_array_almost_equal(actual, expected)
    
    def test_transformer_sum(self):
        ssr = fe.SentiScorer(transform_POS=True, dropna=True, synsets_aggregation='sum')
        actual = ssr.transform(self.data)
        expected = np.array([[ 1.25 ,  0.   ],
                            [ 2.25 ,  9.5  ],
                            [ 0.   ,  0.625],
                            [26.5  ,  0.5  ]])
        np.testing.assert_array_almost_equal(actual, expected)

    def test_get_POS(self):
        ssr = fe.SentiScorer(transform_POS=False, dropna=False, synsets_aggregation='sum')
        actual = ssr.get_POS(self.data[0])
        expected = [('this', 'DT'),
                    ('is', 'VBZ'),
                    ('a', 'DT'),
                    ('wonderful', 'JJ'),
                    ('day', 'NN')]
        self.assertEqual(actual, expected)