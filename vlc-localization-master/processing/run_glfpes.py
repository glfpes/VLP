import sys
import string
import os
if __name__ == '__main__':
	vlccpp_pair = "C:\\Users\\glfpes\\Documents\\GitHub\\VLP\\vlccpp\\vlccpp\\pairs.txt";
	file_object = open(vlccpp_pair);
	cols=2
	rows=5
	image = [[0 for col in range(cols)] for row in range(rows)];
	cols=3
	rows=5
	room =  [[0 for col in range(cols)] for row in range(rows)];
	i=0
	try:
		for line in file_object:
			j=i/5;
			k=i%5;
			number = string.atof(line);
			if(k<2):
				image[j][k]=number
			if(k>1):
				room[j][k-2]=number
			i=i+1;
		lights = [
			(
				image[i],
				(room[i],)
			) for i in xrange(len(image))]
		print lights
	finally:
		file_object.close();



	
