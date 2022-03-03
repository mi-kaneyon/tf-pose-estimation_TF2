# tf-pose-estimation_TF2
Please refer to my reference original "ildoonet-tf-pose-estimation"

This source refrence  is under [jiajunhua repo](https://github.com/jiajunhua/ildoonet-tf-pose-estimation).

And tf-pose-estimation's Openpose', human pose estimation algorithm [Repo](https://github.com/CMU-Perceptual-Computing-Lab/openpose)

# Modification from ildoonet-tf-pose-estimation

* Available to use under tensorflow 2.x
* General code is converted by Tensorflow official notebook except contrib or some specified APIs.
* Some APIs were modified by myself.
* modified main file is runwebcom.py only. if you want to try use other sorce plz modifiy it.

# Preparation and Requirement
1. My test environment
2. Python 3.6.13 and Tensorflow 2.6.2
3. make sure installing "requirement.txt" modules

# Installation additional components
3rd party libraries

```
pip3 install -r requirements.txt

```

Build c++ library for post processing. See :[here](https://github.com/ildoonet/tf-pose-estimation/tree/master/tf_pose/pafprocess)

```
#if you don't install swig yet, try command line bellow (plz remove "#"
#sudo apt -y update 
#sudo apt -y install swig

#under extracted folder
cd tf_pose/pafprocess
swig -python -c++ pafprocess.i && python3 setup.py build_ext --inplace

```

Updating tf_slim if your tf_slim is old version(In my case no need specified version)

```
pip install --upgrade tf_slim

#Already in the tf_pose folders py files replaced from tf.contrib to tf_slim
# In general using
#import tf_slim as slim

```

