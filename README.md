## Setup

You need the cutting-edge [Statechart Virtual Machine](http://msdl.cs.mcgill.ca/people/tfeng/uml/svm.html) to run the watch. Also a version 2.7 Python is mandatory, and you might need to install some tkinter packages to be able to see the GUI.

## Running

Extract your svm, and

```
$ /path/to/svm watch.des
```

When you're done using the watch, make sure you're not running any other Python instances, and simply:

```
$ killall python
```

