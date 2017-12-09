Hello!

The flow of the algorithm is as follows : 
1)Use Encode.py to encode the image and create a file dump as input to modulating gnuradio section
example use: python Encode.py 'path to input image' 'path to start sequence' 'path to stop sequence'
This will generate a file 'Input_Dump'.{You can use your own pilot sequences as Start and Stop Seqeuences, we have added ours here as an example}
2)Use the dump file generated above as an input through the File Source block in gnu radio.
3)The gnu radio code generates an output dump file via the File Sink block
4)Use Decode.py to decode the file dump output of demodulating gnuradio radio section
example use: python Decode.py 'path to output dump' 'path to start sequence' 'path to stop sequence' 'width of image' 'height of image'
This will generate an image 'out.png', which is the decoded image

Comments have been written in the python codes to explain them.

We have also provided a file to test the algorithm, so the code can be run as follows:
1)python Encode.py img.bmp start_sequence.txt stop_sequence.txt
2)Run the above dump as an input to the DBPSK and DQPSK GNU radio codes, and generate an output dump named 'OUTPUT_Dump'
3)python Decode.py OUTPUT_Dump start_sequence.txt stop_sequence.txt 169 179
This will generate the decoded image file.

A brief report('DQPSK.pdf') has also been attached.

Thank You!
