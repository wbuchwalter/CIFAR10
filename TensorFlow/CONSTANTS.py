#!/usr/bin/env python3
"""
Author: David Crook
Copyright Microsoft Corporation 2017
"""

DEBUG = True

IMAGE_SHAPE = (32, 32, 3)
NUM_CLASSES = 10

INPUT_PIPELINE_THREADS = 2
#batch size * minibatches = # samples in data set or greater.
BATCH_SIZE = 100
MINI_BATCHES = 50
EPOCHS = 10
LEARNING_RATE = 1e-6
N_CLASSES = 10

r_bdir = 'C:/data/cifar_10/tfrecords/'
RecordPaths = [
    r_bdir + '1.tfrecords',
    r_bdir + '2.tfrecords',
    r_bdir + '3.tfrecords',
    r_bdir + '4.tfrecords'
]
