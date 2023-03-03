class Rectangle:
    def __init__(self, width=0, height=0):
        self.width=width
        self.height=height

    def set_width(self, value):
        self.width=value
        
    def set_height(self, value):
        self.height=value

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture=''
            for x in range(0,self.height):
                for y in range(0,self.width):
                    picture+='*'
                picture+='\n'
            return picture

    def get_amount_inside(self, picture):
        count=-1
        width_base=self.width
        width_picture=0
        
        while self.width>=width_picture:
            width_picture+=picture.width
            count+=1
            
        width_picture-=picture.width
        new_width=self.width-(self.width-width_picture)
        area_base=self.height*new_width         

        count=0
        while area_base>=picture.get_area():
            area_base-=picture.get_area()
            count+=1
        return count

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'



class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side=side

    def set_side(self,value):
        self.side=value
        self.width=value
        self.height=value
    
    def set_width(self, value):
        self.set_side(value)
        
    def set_height(self, value):
        self.set_side(value)
      

    def __str__(self):
         return f'Square(side={self.side})'
