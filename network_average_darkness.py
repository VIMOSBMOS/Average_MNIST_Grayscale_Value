import mnist_loader
import numpy as np 
import collections
from collections import defaultdict


def average_validation_data():
		training_data, validation_data, test_data = np.asarray(mnist_loader.load_data())
		d1 = defaultdict(int)
		d2 = defaultdict(float)
		# Creating two dictionaries for the average of grayscale values and the frequncies of the digits
		for image_data, digit_frequency_data in zip(training_data[0], training_data[1]):
			d1[digit_frequency_data] += 1
			d2[digit_frequency_data] += image_data.mean(axis=0)

		print(d1)
		print(d2)
		# 
		average = defaultdict(float)
		for key, value_frequency in d1.iteritems():
			average[key] = round((d2[key]/value_frequency),4)
		print(average) 

		# Testing above algorithm on test_data
		count = 0
		for test_image_data, test_label_data in zip(test_data[0], test_data[1]):
			average_grayscale_test_value = round(test_image_data.mean(axis=0),4)
			tolerance = abs(average_grayscale_test_value - average[test_label_data])
			#print(tolerance)
			if (tolerance <=0.0005) :
				#print(tolerance)
				#print(average[test_label_data])
				count += 1
		print(count)







