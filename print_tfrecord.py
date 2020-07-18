import argparse
import os

def print_TFRecord(input_dir):
    import tensorflow as tf

    for example in tf.python_io.tf_record_iterator(input_dir):
      result = tf.train.SequenceExample.FromString(example)
      break
      
    print(result)

def main():
    #Initiate argument parser
    parser = argparse.ArgumentParser(
        description="Print TFRecord"
    )
    parser.add_argument(
        "-i",
        "--inputDir",
        help="Path to folder where TFRecord stored",
        type=str,
    )
    
    args = parser.parse_args()
    
    if args.inputDir is None:
        print("Please specify input argument, eg: python print_tfrecord.py -i=<directory>")
        exit()
        
    print_TFRecord(args.inputDir)
    
if __name__=="__main__":
    main()