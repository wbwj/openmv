import sensor,image, time

sensor.reset()   #重置并初始化传感器
sensor.set_pixformat(sensor.RGB565)  #将像素格式设置为RGB565（或GRAYSCALE）
sensor.set_framesize(sensor.QVGA)    #将帧大小设置为QVGA（320x240）
sensor.skip_frames(30)               #等待设置生效（括号中是等待的帧数）
clock = time.clock()                 #创建一个时钟对象来跟踪FPS


x = 0
y = 0

rgb_white = (255, 0, 0)     #将RGB值赋值给变量

while(True):
    clock.tick()               #更新FPS时钟
    img = sensor.snapshot()    #拍照并返回图像
    img.draw_string(x, y, "Hello World", color = rgb_white)


print(clock.fps())  #注意：OpenMV Cam在连接时运行速度大约快一半
                    #到IDE。 一旦断开，FPS应该增加
