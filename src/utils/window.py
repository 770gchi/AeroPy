class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.ratio = width / height
        self.w = width
        self.h = height
        self.r = width / height
        self.viewport_width = width
        self.viewport_height = height * 0.79
        self.vw = width
        self.vh = height * 0.79
        self.viewport_ratio = self.vw / self.vh
        self.vr = self.vw / self.vh



'''用于管理窗口的基本参数，包括宽度、高度以及窗口和视口的宽高比'''