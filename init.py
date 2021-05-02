import afl
import os,sys
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = "2"
import tensorflow as tf

afl.init()

try:
    exec(open("./target/linear_regression.py").read())
except Exception as e:
    pass
#while afl.loop(10):
    #exec(open("linear_regression.py").read())

os._exit(0)
