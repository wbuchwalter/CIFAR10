#!/usr/bin/env python3
"""
Author: David Crook
Copyright Microsoft Corporation 2017
"""

import tensorflow as tf
import LayerDefinitions as ld
import CONSTANTS

class Vgg9Model:
    '''
    Modified Vgg9 network; removed pooling layers.
    '''

    NUM_DENSE_NEURONS = 50

    def inference(images):
        '''
        Portion of the compute graph that takes an input and converts it into a Y output
        '''
        with tf.variable_scope('Conv1') as scope:
            C_1_1 = ld.cnn_layer(images, (5, 5, 3, 32), (1, 1, 1, 1), scope, name_postfix='1')
            C_1_2 = ld.cnn_layer(C_1_1, (5, 5, 32, 32), (1, 1, 1, 1), scope, name_postfix='2')
        with tf.variable_scope('Conv2') as scope:
            C_2_1 = ld.cnn_layer(C_1_2, (5, 5, 32, 32), (1, 1, 1, 1), scope, name_postfix='1')
            C_2_2 = ld.cnn_layer(C_2_1, (5, 5, 32, 32), (1, 1, 1, 1), scope, name_postfix='2')
        with tf.variable_scope('Conv3') as scope:
            C_3_1 = ld.cnn_layer(C_2_2, (5, 5, 32, 32), (1, 1, 1, 1), scope, name_postfix='1')
            C_3_2 = ld.cnn_layer(C_3_1, (5, 5, 32, 32), (1, 1, 1, 1), scope, name_postfix='2')
            P_3 = ld.pool_layer(C_3_2, (1, 2, 2, 1), (1, 2, 2, 1), scope)
        with tf.variable_scope('Dense1') as scope:
            P_3 = tf.reshape(P_3, (-1, self.DENSE_RESHAPE))
            dim = P_3.get_shape()[1].value
            D_1 = ld.mlp_layer(P_3, dim, NUM_DENSE_NEURONS, scope, act_func=tf.nn.relu)
        with tf.variable_scope('Dense2') as scope:
            D_2 = ld.mlp_layer(D_1, NUM_DENSE_NEURONS, CONSTANTS.NUM_CLASSES, scope)
        H = tf.nn.softmax(D_2, name='prediction')
        return H

    def loss(logits, labels):
        '''
        Adds Loss to all variables
        '''
        cross_entr = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=labels)
        cross_entr = tf.reduce_mean(cross_entr)
        tf.summary.scalar('cost', cross_entr)
        tf.add_to_collection('losses', cross_entr)
        return tf.add_n(tf.get_collection('losses'), name='total_loss')
