import os    #os，与操作系统相关的功能，可以处理文件和目录这些日常手动需要做的操作，如：显示当前目录下所有文件/删除某个文件/获取文件大小
import numpy as np
import matplotlib   #matplotlib是python中的一个绘图库，基于matlab
if os.name == 'posix' and "DISPLAY" not in os.environ:   #os.name当前对象所对应的环境
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
else:
    import matplotlib.pyplot as plt
import matplotlib.patches as patches # matplotlib.patches包里面存放有各种形状（椭圆、箭头。。。）


def show_frame(frame, bbox, fig_n, pause=2):
    plt.ion()  #python可视化库matplotlib的显示模式默认为阻塞（block）模式，即在plt.show()之后，程序会暂停到那儿，并不会继续执行下去。
               #如果需要继续执行程序，就要关闭图片。那如何展示动态图或多个窗口呢？
               #这就要使用plt.ion()这个函数，使matplotlib的显示模式转换为交互（interactive）模式。即使在脚本中遇到plt.show()，代码还是会继续执行
    plt.clf()  #Clear figure清除所有轴，但是窗口打开，这样它可以被重复使用
    fig = plt.figure(fig_n)  #打开图形窗口
    ax = fig.gca()   #返回坐标轴
    r = patches.Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3], linewidth=2, edgecolor='r', fill=False)
     #绘制矩形，bbox[0],bbox[1]表示矩形左下角xy坐标，bbox[2]表示长、bbox[3]表示宽，红色线条，无填充
    ax.imshow(np.uint8(frame))
    ax.add_patch(r)
    fig.show()
    fig.canvas.draw() #属性修改之后并不会立即反映到图表的显示上，还需要调用fig.canvas.draw()函数才能够更新显示
    plt.pause(pause)


def show_frame_and_response_map(frame, bbox, fig_n, crop_x, score, pause=2):
    fig = plt.figure(fig_n)
    ax = fig.add_subplot(131)    
    ax.set_title('Tracked sequence')
    r = patches.Rectangle((bbox[0],bbox[1]), bbox[2], bbox[3], linewidth=2, edgecolor='r', fill=False)
    ax.imshow(np.uint8(frame))
    ax.add_patch(r)       #定义图一（模板）
    ax2 = fig.add_subplot(132)
    ax2.set_title('Context region')
    ax2.imshow(np.uint8(crop_x))
    ax2.spines['left'].set_position('center')
    ax2.spines['right'].set_color('none')
    ax2.spines['bottom'].set_position('center')
    ax2.spines['top'].set_color('none')
    ax2.set_yticklabels([])
    ax2.set_xticklabels([])    #定义图二（样本）
    ax3 = fig.add_subplot(133)
    ax3.set_title('Response map')
    ax3.spines['left'].set_position('center')
    ax3.spines['right'].set_color('none')
    ax3.spines['bottom'].set_position('center')
    ax3.spines['top'].set_color('none')
    ax3.set_yticklabels([])
    ax3.set_xticklabels([])
    ax3.imshow(np.uint8(score))   #定义图三（得分图）

    plt.ion()
    plt.show()
    plt.pause(pause)
    plt.clf()


def save_frame_and_response_map(frame, bbox, fig_n, crop_x, score, writer, fig):
    # fig = plt.figure(fig_n)
    plt.clf()
    ax = fig.add_subplot(131)
    ax.set_title('Tracked sequence')
    r = patches.Rectangle((bbox[0],bbox[1]), bbox[2], bbox[3], linewidth=2, edgecolor='r', fill=False)
    ax.imshow(np.uint8(frame))
    ax.add_patch(r)
    ax2 = fig.add_subplot(132)
    ax2.set_title('Context region')
    ax2.imshow(np.uint8(crop_x))
    ax2.spines['left'].set_position('center')
    ax2.spines['right'].set_color('none')
    ax2.spines['bottom'].set_position('center')
    ax2.spines['top'].set_color('none')
    ax2.set_yticklabels([])
    ax2.set_xticklabels([])
    ax3 = fig.add_subplot(133)
    ax3.set_title('Response map')
    ax3.spines['left'].set_position('center')
    ax3.spines['right'].set_color('none')
    ax3.spines['bottom'].set_position('center')
    ax3.spines['top'].set_color('none')
    ax3.set_yticklabels([])
    ax3.set_xticklabels([])
    ax3.imshow(np.uint8(score))

    # ax3.grid()
    writer.grab_frame()


def show_crops(crops, fig_n):
    fig = plt.figure(fig_n)
    ax1 = fig.add_subplot(131)
    ax2 = fig.add_subplot(132)
    ax3 = fig.add_subplot(133)
    ax1.imshow(np.uint8(crops[0,:,:,:]))
    ax2.imshow(np.uint8(crops[1,:,:,:]))
    ax3.imshow(np.uint8(crops[2,:,:,:]))
    plt.ion()
    plt.show()
    plt.pause(0.001)


def show_scores(scores, fig_n):
    fig = plt.figure(fig_n)
    ax1 = fig.add_subplot(131)
    ax2 = fig.add_subplot(132)
    ax3 = fig.add_subplot(133)
    ax1.imshow(scores[0,:,:], interpolation='none', cmap='hot')
    ax2.imshow(scores[1,:,:], interpolation='none', cmap='hot')
    ax3.imshow(scores[2,:,:], interpolation='none', cmap='hot')
    plt.ion()
    plt.show()
    plt.pause(0.001)
