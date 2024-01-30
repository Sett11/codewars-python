class DimensionsOutOfBoundError(Exception):
    def __init__(self,text):
        self.text=text

class Package:
    def __init__(self,length,width,hieght,weight):
        self._length=length
        self._width=width
        self._height=hieght
        self._weight=weight
        self._volume=self._length*self._width*self._height
        self.text="Package {0}=={1} out of bounds, should be: {2} < {3} <= {4}"
        if self.length<=0 or self.length>350:
            raise(DimensionsOutOfBoundError(self.text.format('length',self.length,0,'length',350)))
        if self.width<=0 or self.width>300:
            raise(DimensionsOutOfBoundError(self.text.format('width',self.width,0,'width',300)))
        if self.height<=0 or self.height>150:
            raise(DimensionsOutOfBoundError(self.text.format('height',self.height,0,'height',150)))
        if self.weight<=0 or self.weight>40:
            raise(DimensionsOutOfBoundError(self.text.format('weight',self.weight,0,'weight',40)))
    
    @property
    def volume(self):
        return self._length*self._width*self._height
    
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self,value):
        if value<=0 or value>350:
            raise(DimensionsOutOfBoundError(self.text.format('length',value,0,'length',350)))
        self._length=value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        if value<=0 or value>300:
            raise(DimensionsOutOfBoundError(self.text.format('width',value,0,'width',300)))
        self._width=value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        if value<=0 or value>150:
            raise(DimensionsOutOfBoundError(self.text.format('height',value,0,'height',150)))
        self._height=value
    
    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self,value):
        if value<=0 or value>40:
            raise(DimensionsOutOfBoundError(self.text.format('weight',value,0,'weight',40)))
        self._weight=value

inputs = (0.2, 0.2, 0.2, 0.2)
p = Package(*inputs)

print(p.volume)