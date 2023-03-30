import argparse

from moviepy.editor import *


def opt_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, default='', help='The path to the video file, either absolute or relative')
    parser.add_argument('--resize', type=str, default=None,
                        help='Modify the size and accept a tuple or a value between 0 and 1. For example, (300, 200) means that the size is converted to 300 wide by 200 high, and 0.5 means that the size is scaled to half')
    parser.add_argument('--fps', type=int, default=None,
                        help='Pumping frames and accept integers. For example 20 means generating the mp4 as a Gif at 20 frames per second')
    parser.add_argument('--clip', type=str, default=None,
                        help='Video crop and accept tuple. For example (3, 10) means crop video between 3-10 seconds to generate Gif')
    opt = parser.parse_args()
    return opt


class Mp42GifOp(object):
    def __init__(self, resize=None, fps=None, clip=None):
        """
        :param resize: 修改尺寸，接收元组或者0-1之间的值，比如 (300, 200) 的意思是尺寸转为宽300高200，0.5 的意思是尺寸缩放到一半
        :param fps: 抽帧，接收整数，比如 20 的意思就是将mp4生成每秒 20 帧的gif
        :param clip: 视频裁剪，接收元组，比如 (3, 10) 的意思是裁剪 3-10 秒之间的视频生成gif
        """
        self.resize = resize
        self.fps = fps
        self.clip = clip

    def mp42gif(self, mp4path, gifpath):
        vfc = VideoFileClip(mp4path)
        if self.clip:
            vfc = vfc.subclip(*eval(self.clip))
        if self.resize:
            vfc = vfc.resize(eval(self.resize))
        clip = (vfc)
        if self.fps:
            clip.write_gif(gifpath, fps=self.fps)
        else:
            clip.write_gif(gifpath)
        print("{} to {} complete!".format(mp4path, gifpath))


if __name__ == '__main__':
    opt = opt_argparse()
    # 初始化
    m2g = Mp42GifOp(opt.resize, opt.fps, opt.clip)
    # 生成gif路径
    spl = opt.path.replace('\\', '/').rsplit('/', 1)
    if len(spl) == 1:
        gifname = spl[0].rsplit('.', 1)[0]
        path = ''
    else:
        gifname = spl[1].rsplit('.', 1)[0]
        path = spl[0]
    gif_path = os.path.join(path, '{}.{}'.format(gifname, 'gif'))
    print(opt.path, gif_path)
    # 转换
    m2g.mp42gif(opt.path, gif_path)
