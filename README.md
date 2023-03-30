# Convenient-Tools-With-Python

This project involves all kinds of practical and convenient tools written in Python.

* **Video2Gif.py** : used to convert video files to GIF animations

## 1. Video2Gif.py

* Open the terminal and enter the following command to install the python libraries required by this document.

  ```shell
  pip install moviepy 
  ```

* Continue to enter the following command to convert the corresponding video file to Gif animation, the Gif file is saved in the same directory as the video file.

  ```shell
  python Video2Gif.py --path 1.mp4 --resize (200,500) --fps 10 --clip (3,10)  
                                              0.5                                    
  ```

* Parameter description in the command:

  * **path** : `The path to the video file, either absolute or relative.`
  * **resize** : `Modify the size and accept a tuple or a value between 0 and 1. For example, (300, 200) means that the size is converted to 300 wide by 200 high, and 0.5 means that the size is scaled to half.`
  * **fps** : `Pumping frames and accept integers. For example 20 means generating the mp4 as a Gif at 20 frames per second.`
  * **clip** : `Video crop and accept tuple. For example (3, 10) means crop video between 3-10 seconds to generate Gif.`