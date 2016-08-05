#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
word2vecをtensorflowを使って実装する
"""
from itertools import izip
import random
import math
import collections
import tensorflow as tf
import numpy as np

class Word2Vec:
    def __init__(self):
        self.vocabulary_size = 50000
        self.embedding_size = 128
        self.batch_size = 128
        self.num_skips = 2
        self.skip_window = 1
        self.data_index = 0
        self.valid_size = 16
        self.valid_window = 100
        self.num_sampled = 64

        self.words = []
        with open("_combined.txt", "rb") as infile:
            l = infile.readline()
            while l:
                self.words += l.split()
                l = infile.readline()
        self.data = None
        self.count = None
        self.dictionary = None
        self.reverse_dictionary = None
        self.graph = None
        self.train_inputs = None
        self.train_labels = None
        self.init = None
        self.optimizer = None
        self.loss = None


    def build_dataset(self):
        count = [['UNK', -1]]
        count.extend(collections.Counter(self.words).most_common(self.vocabulary_size - 1))
        dictionary = dict()
        for word, _ in count:
            dictionary[word] = len(dictionary)
        data = list()
        unk_count = 0
        for word in self.words:
            if word in dictionary:
                index = dictionary[word]
            else:
                index = 0  # dictionary['UNK']
                unk_count += 1
        data.append(index)
        count[0][1] = unk_count
        reverse_dictionary = dict(izip(dictionary.values(), dictionary.keys()))
        self.data, self.count, self.dictionary, self.reverse_dictionary = data, count, dictionary, reverse_dictionary
        del self.words # release memory


    def generate_batch(self):
        batch = np.ndarray(shape=(self.batch_size), dtype=np.int32)
        labels = np.ndarray(shape=(self.batch_size, 1), dtype=np.int32)
        span = 2 * self.skip_window + 1 # [ self.skip_window target self.skip_window ]
        buffer = collections.deque(maxlen=span)
        for _ in range(span):
            buffer.append(self.data[self.data_index])
            self.data_index = (self.data_index + 1) % len(self.data)
        for i in range(self.batch_size // self.num_skips):
            target = self.skip_window  # target label at the center of the buffer
            targets_to_avoid = [ self.skip_window ]
        for j in range(self.num_skips):
            while target in targets_to_avoid:
                target = random.randint(0, span - 1)
            targets_to_avoid.append(target)
            batch[i * self.num_skips + j] = buffer[self.skip_window]
            labels[i * self.num_skips + j, 0] = buffer[target]
        buffer.append(self.data[self.data_index])
        self.data_index = (self.data_index + 1) % len(self.data)
        return batch, labels


    def set_graph(self):
        self.graph = tf.Graph()
        valid_examples = np.random.choice(self.valid_window, self.valid_size, replace=False)
        with self.graph.as_default():

            self.train_inputs = tf.placeholder(tf.int32, shape=[self.batch_size])
            self.train_labels = tf.placeholder(tf.int32, shape=[self.batch_size, 1])
            valid_dataset = tf.constant(valid_examples, dtype=tf.int32)

            embeddings = tf.Variable(
                tf.random_uniform([self.vocabulary_size, self.embedding_size], -1.0, 1.0))
            embed = tf.nn.embedding_lookup(embeddings, self.train_inputs)

            nce_weights = tf.Variable(
                tf.truncated_normal([self.vocabulary_size, self.embedding_size],
                                    stddev=1.0 / math.sqrt(self.embedding_size)))
            nce_biases = tf.Variable(tf.zeros([self.vocabulary_size]))

            self.loss = tf.reduce_mean(
                tf.nn.nce_loss(nce_weights, nce_biases, embed, self.train_labels,
                               self.num_sampled, self.vocabulary_size))

            self.optimizer = tf.train.GradientDescentOptimizer(1.0).minimize(self.loss)

            norm = tf.sqrt(tf.reduce_sum(tf.square(embeddings), 1, keep_dims=True))
            normalized_embeddings = embeddings / norm
            valid_embeddings = tf.nn.embedding_lookup(
                normalized_embeddings, valid_dataset)
            similarity = tf.matmul(
                valid_embeddings, normalized_embeddings, transpose_b=True)

            self.init = tf.initialize_all_variables()

    def training(self):
        num_steps = 100001
        with tf.Session(graph=self.graph) as session:
            self.init.run()
            print "Initialized"

            average_loss = 0
            for step in xrange(num_steps):
                batch_inputs, batch_labels = self.generate_batch()
                feed_dict = {self.train_inputs : batch_inputs, self.train_labels : batch_labels}

                _, loss_val = session.run([self.optimizer, self.loss], feed_dict=feed_dict)
                average_loss += loss_val

                # if step % 2000 == 0:
                #     if step > 0:
                #     average_loss /= 2000
                #     print "Average loss at step %s: %s" % (step, average_loss)
                #     average_loss = 0

                # if step % 10000 == 0:
                #     sim = similarity.eval()
                #     for i in xrange(valid_size):
                #         valid_word = reverse_dictionary[valid_examples[i]]
                #         top_k = 8 # number of nearest neighbors
                #         nearest = (-sim[i, :]).argsort()[1:top_k+1]
                #         log_str = "Nearest to %s:" % valid_word
                #     for k in xrange(top_k):
                #         close_word = reverse_dictionary[nearest[k]]
                #         log_str = "%s %s," % (log_str, close_word)
                #     print log_str
                # final_embeddings = normalized_embeddings.eval()



w2v = Word2Vec()
w2v.build_dataset()
w2v.set_graph()
w2v.training()

