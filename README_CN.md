# Convenient-Tools-With-Python

本项目主要包含了使用Python编写的各类便捷小工具，主要有如下内容：

* **Video2Gif.py** : 用于将视频文件转换成Gif动画

## 1. Video2Gif.py

* 打开终端，输入如下命令，安装本文件所需的第三方库。

  ```shell
  pip install moviepy 
  ```

* 继续输入以下命令，即可将对应的视频文件转换成Gif动画，Gif文件保存在与视频文件同一个目录下。

  ```shell
  python Video2Gif.py --path 1.mp4 --resize (200,500) --fps 10 --clip (3,10)  
                                              0.5                                    
  ```

* 命令中的参数说明:

  * **path** : `视频文件的路径，可以是绝对路径，也可以是相对路径。`
  * **resize** : `修改尺寸，接收元组或者0-1之间的值，比如 (300, 200) 的意思是尺寸转为宽300高200，0.5 的意思是尺寸缩放到一半。`
  * **fps** : `抽帧，接收整数，比如 20 的意思就是将mp4生成每秒 20 帧的Gif。`
  * **clip** : `视频裁剪，接收元组，比如 (3, 10) 的意思是裁剪 3-10 秒之间的视频生成Gif。`