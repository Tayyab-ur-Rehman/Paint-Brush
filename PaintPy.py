from tkinter import *  
import string
import math
import webcolors
from PIL import Image,ImageTk
import PIL.ImageGrab as ImageGrab
from tkinter import filedialog
from tkinter import messagebox  
from tkinter import colorchooser                                                                                                                                                                                            
class PaintBrush:
    def __init__(self,w,hei,title):
        self.screen=Tk()
        self.b_colour="black"
        self.fill_col="black"
        self.n=4
        self.width=5
        self.screen.title(title)
        self.rt_id=None
        self.screen.geometry(str(w)+'x'+str(hei))
        #eraser
        self.eraser_col='white'
        self.eraser_width=5
        #buttons area
        self.button_area=Frame(self.screen,width=w,height=75,bg="gray")
        self.button_area.pack()
        #buttons
        #clear
        self.clear_button=Button(self.button_area,text="Clear ",command=self.clear_canvas)
        self.clear_button.place(x=5,y=5)
         #Stright line
        self.line_button=Button(self.button_area,text="Line",command=self.pressed_line)
        self.line_button.place(x=55,y=5)
        #brush
        self.brush_button=Button(self.button_area,text="                 Brush                  ",command=self.brush_pressed)
        self.brush_button.place(x=650,y=5)
        #rectangle
        self.rectangle_button=Button(self.button_area,text="rectangle",command=self.pressed_rectangle)
        self.rectangle_button.place(x=100,y=5)
         #square
        self.square_button=Button(self.button_area,text="square",command=self.pressed_square)
        self.square_button.place(x=170,y=5)
        # Circle
        self.Circle_button=Button(self.button_area,text="Circles",command=self.pressed_circle)
        self.Circle_button.place(x=5,y=40)
        # Triangle
        self.Triangle_button=Button(self.button_area,text=" Triangle ",command=self.pressed_triangle)
        self.Triangle_button.place(x=100,y=40)
        # Star
        self.star_button=Button(self.button_area,text="Star ",command=self.pressed_star)
        self.star_button.place(x=55,y=40)
        #oval
        self.oval_button=Button(self.button_area,text=" Oval  ",command=self.pressed_oval)
        self.oval_button.place(x=170,y=40) 
        #4 buttons for width
        self.w3_button=Button(self.button_area,text=" 3 ",command=self.width_setterr3)
        self.w3_button.place(x=650,y=40) 

        self.w5_button=Button(self.button_area,text=" 5 ",command=self.width_setterr5)
        self.w5_button.place(x=685,y=40) 

        self.w10_button=Button(self.button_area,text=" 10 ",command=self.width_setterr10)
        self.w10_button.place(x=720,y=40) 

        self.w15_button=Button(self.button_area,text=" 15 ",command=self.width_setterr15)
        self.w15_button.place(x=760,y=40) 
        # Polygon
        tex="   Polygon   "
        self.Pentagon_button=Button(self.button_area,text=tex,command=self.pressed_polygon)
        self.Pentagon_button.place(x=230,y=5) 
        # select n
        self.n_var=Entry(self.button_area,width=5)
        self.n_var.place(x=230,y=40) 
        tex="n ="+str(self.n)
        self.n_var.insert(0,tex)
        self.n_var.get()
        #Eneter button
        self.Enter_button=Button(self.button_area,text="Enter",command=self.Enter_n_pressed,bg='black',fg='white',height=1)
        self.Enter_button.place(x=270,y=35)
        #colour palette
        self.s_colour_button=Button(self.button_area,command=self.select_col,border=3,width=5)
        self.s_colour_button.configure(bg=self.b_colour)  
        self.s_colour_button.place(x=330,y=5) 
        #fill colour palette
        self.fs_colour_button=Button(self.button_area,command=self.select_col_fill,border=3,width=5)
        self.fs_colour_button.configure(bg=self.fill_col)  
        self.fs_colour_button.place(x=330,y=40) 
        #fill colour
        self.colour_button=Button(self.button_area,text="    FILL COLOR      ",command=self.pressed_fill_colour,bg='black',fg='white')  
        self.colour_button.place(x=800,y=40)
        #Boundry colour
        self.Boundry_colour_button=Button(self.button_area,text=" Boundry COLOR ",command=self.pressed_boundry_colour,bg='black',fg='white')
        self.Boundry_colour_button.place(x=800,y=5)
        #eraser
        # to be set
        self.eraser_button=Button(self.button_area,text=" ERASER ",bg='red',fg='white',border=5,width=25)
        self.eraser_button.place(x=920,y=5)
        #self.eraser_button.pack()
        self.eraser_button.bind( "<Button-1>", self.pressed_eraser)
        self.eraser_button.bind("<Double-Button-1>", self.eraser_pallete)
        #slide_erase
        erase_slide=Scale(self.button_area,from_=3,to=30,showvalue=0,orient='horizontal',length=185,bg='pink',fg='black',command=self.update_era_width)
        erase_slide.grid(row=5,column=50,padx=1000,pady=25)
        erase_slide.place(x=920,y=39,height=25)
        
        #save button
        self.save_button=Button(self.button_area,text=" Download Canvas ",command=self.save_canvas,border=6)
        self.save_button.configure(bg="green", activebackground="green")  
        self.save_button.place(x=1220,y=5) 
        #load button                                   " Download Canvas "
        self.savel_button=Button(self.button_area,text="       Load Canvas    ",command=self.load_canvas,border=6)
        self.savel_button.configure(bg="green", activebackground="green")  
        self.savel_button.place(x=1220,y=40) 
        #zoom in button
        self.zoomIn_button=Button(self.button_area,text="    Zoom In     ",command=self.zoomIn,border=6)
        self.zoomIn_button.configure(bg="yellow", activebackground="pink")  
        self.zoomIn_button.place(x=1120,y=5) 
        #zoom out button
        self.zoomOutbutton=Button(self.button_area,text="   Zoom out   ",command=self.zoomOut,border=6)
        self.zoomOutbutton.configure(bg="yellow", activebackground="pink")  
        self.zoomOutbutton.place(x=1120,y=40) 
        #cut
        self.cut_button=Button(self.button_area,text="      Cut  Object      ",command=self.pressed_cut,fg='white',bg='red')
        self.cut_button.place(x=530,y=5)
        self.cut_done=FALSE
         #curve
        self.curve_button=Button(self.button_area,text="    Benzile   Curve       ",command=self.pressed_curve,fg='white',bg='blue')
        self.curve_button.place(x=400,y=5)
        #colour giver
        self.colour_giver=Button(self.button_area,text=" Pexel Picker colour ",command=self.get_pixel_click,fg='black',bg='pink')
        self.colour_giver.place(x=400,y=45)
        #button colour
        self.red_fill=Button(self.button_area,command=self.fill_red,fg='black',bg='red',width=2)
        self.red_fill.place(x=570,y=45)
        #green
        self.green_fill=Button(self.button_area,command=self.fill_green,fg='black',bg='green',width=2)
        self.green_fill.place(x=530,y=45)
        #blue
        self.blue_fill=Button(self.button_area,command=self.fill_blue,fg='black',bg='blue',width=2)
        self.blue_fill.place(x=610,y=45)
        #points
        self.last_x=None
        self.last_y=None
        #canvas 
        self.canvas=Canvas(self.screen,w=w-50,height=hei-50,bg="white") 
        self.canvas.pack()
        #self.col_2lable=Label(self.canvas,Text="k",bg=self.fill_col)
        #self.col_2lable()
        self.point_used=[]
        #bind
        self.canvas.bind("<B1-Motion>",self.brush_draw)
        self.canvas["cursor"] = "pencil"
        self.canvas.bind("<ButtonRelease-1>",self.draw_shapes_end)
    def fill_red(self):
        self.fill_col='red'
        self.fs_colour_button.configure(bg=self.fill_col)  
    def fill_green(self):
        self.fill_col='green'
        self.fs_colour_button.configure(bg=self.fill_col)  
    def fill_blue(self):
        self.fill_col='blue'
        self.fs_colour_button.configure(bg=self.fill_col)  
    def update_era_width(self,value):
        self.eraser_width=int(value  )  
    def width_setterr3(self):
        self.width=3
    def width_setterr5(self):
        self.width=5
    def width_setterr10(self):
        self.width=10
    def width_setterr15(self):
        self.width=15
    def brush_pressed(self):
        self.canvas["cursor"] = "pencil"
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.brush_draw)
        self.canvas.bind("<ButtonRelease-1>",self.draw_shapes_end)
    def Enter_n_pressed(self):
        b=self.n_var.get()
        a=int(b)
        if(a>2 and a<100):
            self.n=a
            tex="n ="
            self.n_var.insert(0,"")
            self.n_var.insert(0,tex)
    def pressed_cut(self):
        self.canvas["cursor"] = "hand2"
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<Button-1>")
        #self.canvas.bind("<B1-Motion>",self.cut_section)
        #@self.canvas.bind("<ButtonRelease-1>",self.cut_section)
        self.canvas.bind("<Button-1>",self.cut_)
    def pressed_curve(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<Button-1>")
        self.canvas.bind("<Button-1>",self.Points_curve)
    def pressed_eraser(self,event):
        self.canvas["cursor"] = DOTBOX
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<Button-1>")
        self.canvas.bind("<B1-Motion>",self.eraser)
        self.canvas.bind("<ButtonRelease-1>",self.draw_shapes_end)
    def pressed_fill_colour(self):
        self.canvas["cursor"] = "hand1"
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<Button-1>")
        self.canvas.bind("<Button-1>",self.fill_colour)
    def pressed_boundry_colour(self):
        self.canvas["cursor"] = "hand2"
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<Button-1>")
        self.canvas.bind("<Button-1>",self.boundry_colour)
    def boundry_colour(self,event):
        x=event.x
        y=event.y
        closest_obj = self.canvas.find_closest(x, y)
        if(closest_obj!=1):
          self.canvas.itemconfig(closest_obj, outline=self.b_colour)
    def pressed_line(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<Button-1>")
        self.canvas.bind("<B1-Motion>",self.draw_line)
        self.canvas.bind("<ButtonRelease-1>",self.draw_shapes_end)
    def pressed_triangle(self):
        self.canvas["cursor"] = "crosshair"
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<Button-1>")
        self.canvas.bind("<B1-Motion>",self.draw_triangle)
        self.canvas.bind("<ButtonRelease-1>",self.draw_shapes_end)
    def pressed_star(self):
        self.canvas["cursor"] = "crosshair"
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<Button-1>")
        self.canvas.bind("<B1-Motion>",self.draw_star)
        self.canvas.bind("<ButtonRelease-1>",self.draw_shapes_end)
    def pressed_rectangle(self):
        self.canvas["cursor"] = "crosshair"
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<Button-1>")
        self.canvas.bind("<B1-Motion>",self.draw_rectangle)
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<ButtonRelease-1>",self.draw_shapes_end)
    def pressed_square(self):
        self.canvas["cursor"] = "crosshair"
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<Button-1>")
        self.canvas.bind("<B1-Motion>",self.draw_square)
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<ButtonRelease-1>",self.draw_shapes_end)
    def pressed_polygon(self):
        self.canvas["cursor"] = "crosshair"
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<Button-1>")
        self.canvas.bind("<B1-Motion>",self.draw_polygon)
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<ButtonRelease-1>",self.draw_shapes_end)
    def eraser_pallete(self,event):
        selected_colour=colorchooser.askcolor()
        if(selected_colour[1]!=None):  
                self.eraser_col=selected_colour[1] 
    def get_pixel_click(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<Button-1>",self.get_pixel_color_bg) 
    def get_pixel_color_bg(self,event):
        # Grab the screen image
        image = ImageGrab.grab()
        pixel_color = image.getpixel((event.x, event.y+130))
        print(pixel_color)
        if(pixel_color!=()):
             closest_color = webcolors.rgb_to_name(pixel_color)
             self.fill_col=  closest_color
             print(closest_color)
        #print(closest_color)
             self.fs_colour_button.configure(bg=self.fill_col)  
    def pressed_circle(self):
        self.canvas["cursor"] = "crosshair"
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<Button-1>")
        self.canvas.bind("<B1-Motion>",self.draw_circle)
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<ButtonRelease-1>",self.draw_shapes_end)
    def pressed_oval(self):
        self.canvas["cursor"] = "crosshair"
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<Button-1>")
        self.canvas.bind("<B1-Motion>",self.draw_oval)
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<ButtonRelease-1>",self.draw_shapes_end)
    def fill_colour(self,event):
        x=event.x
        y=event.y
        #closest_obj = self.canvas.find_closest(x, y)
        closest_obj = self.canvas.find_overlapping(x, y,x,y)
        #print(closest_obj)
        if(closest_obj!=()):
                tuple_len=len(closest_obj)
                if(tuple_len==1):
                  self.canvas.itemconfig(closest_obj, fill=self.fill_col)
                else:
                    self.canvas.itemconfig(closest_obj[0], fill=self.fill_col)
        else:
            self.canvas.config(bg=self.fill_col)
    def fill_colour2(self,event):
        x=event.x
        y=event.y
        
        current_colour=self.get_pixel_color(x,y)

        pass
    def draw_star(self,event):
        if(self.rt_id!=None):
           self.canvas.delete(self.rt_id)
        if(self.last_x==None):
            self.last_x= event.x
            self.last_y= event.y
            return
        points = [] 
        length_1=event.x-self.last_x
        length_2=length_1/4
        points.append((self.last_x,self.last_y))
        points.append((self.last_x+1.3*length_2,self.last_y+length_1))
        points.append((self.last_x+length_2+length_1,self.last_y+length_1))  
        points.append((self.last_x+2*length_2,self.last_y+length_1*1.6)) 
        points.append((self.last_x+length_2+length_1*0.5,self.last_y+length_1*1.5+length_1)) 
        points.append((self.last_x,self.last_y+length_1+length_1))
        points.append((self.last_x-2.9*length_2,self.last_y+length_1*1.5+length_1)) 
        points.append((self.last_x-2*length_2,self.last_y+length_1*1.6))
        points.append((self.last_x-length_2-length_1,self.last_y+length_1))  
        points.append((self.last_x-length_2*1.2,self.last_y+length_1))  
        self.rt_id= self.canvas.create_polygon(points,outline=self.b_colour,fill="",width=self.width)
    def draw_circle(self,event):
        if(self.rt_id!=None):
            self.canvas.delete(self.rt_id)
        if(self.last_x==None):
            self.last_x= event.x
            self.last_y= event.y
            return
        radius=abs( self.last_x-event.x)+abs( self.last_y- event.y)
        x1,y1=(self.last_x-radius),(self.last_y-radius)
        x2,y2=(self.last_x+radius),(self.last_y+radius) 
        self.rt_id= self.canvas.create_oval(x1,y1,x2,y2,outline=self.b_colour,width=self.width)
    def draw_oval(self,event):
        if(self.rt_id!=None):
            self.canvas.delete(self.rt_id)
        if(self.last_x==None):
            self.last_x= event.x
            self.last_y= event.y
            return
        radius=abs( self.last_x-event.x)+abs( self.last_y- event.y)
        x1,y1=(self.last_x),(self.last_y)
        x2,y2=(event.x),(event.y) 
        self.rt_id= self.canvas.create_oval(x1,y1,x2,y2,outline=self.b_colour,width=self.width)
    def draw_polygon(self,event):
        if(self.rt_id!=None):
           self.canvas.delete(self.rt_id)
        if(self.last_x==None):
            self.last_x= event.x
            self.last_y= event.y
            return
        points = []
        angle = 2 * math.pi / self.n
        side_length=int(self.last_x)-int(event.x)
        for i in range(self.n):
            x =  self.last_x + side_length * math.cos(i * angle)
            y =  self.last_y + side_length * math.sin(i * angle)
            points.append((x, y))
        self.rt_id= self.canvas.create_polygon(points,outline=self.b_colour,fill="",width=self.width)
    def draw_shapes_end(self,event):
        self.last_x=None
        self.last_y=None
        self.rt_id=None  
    def draw_rectangle(self,event):
        if(self.rt_id!=None):
           self.canvas.delete(self.rt_id)
        if(self.last_x==None):
            self.last_x= event.x
            self.last_y= event.y
            return
        x= self.last_x-event.x
        y=self.last_y-event.y
        self.rt_id= self.canvas.create_rectangle( self.last_x, self.last_y,event.x,event.y,outline=self.b_colour,width=self.width)                                
    def draw_triangle(self,event):
        if(self.rt_id!=None):
           self.canvas.delete(self.rt_id)
        if(self.last_x==None):
            self.last_x= event.x
            self.last_y= event.y
            return
        x= (event.x-self.last_x)
        self.rt_id= self.canvas.create_polygon(self.last_x, self.last_y,event.x,event.y,event.x-2*x,event.y,outline=self.b_colour,width=self.width,fill="")
    def draw_square(self,event):
        if(self.rt_id!=None):
           self.canvas.delete(self.rt_id)
        if(self.last_x==None):
            self.last_x= event.x
            self.last_y= event.y
            return
        x= (event.x-self.last_x)
        y=(event.y-self.last_y)
        self.rt_id= self.canvas.create_rectangle( self.last_x, self.last_y,self.last_x+x, self.last_y+x,outline=self.b_colour,width=self.width)
    def draw_line(self,event):
        if(self.rt_id!=None):
           self.canvas.delete(self.rt_id)
        if(self.last_x==None):
            self.last_x= event.x
            self.last_y= event.y
            return
        self.rt_id= self.canvas.create_line(self.last_x,self.last_y,event.x,event.y,fill=self.b_colour,width=self.width)   
    def select_col(self):
        selected_colour=colorchooser.askcolor()
        if(selected_colour[1]!=None):  
                self.b_colour=selected_colour[1] 
                self.s_colour_button.configure(bg=self.b_colour)  
    def select_col_fill(self):
        selected_colour=colorchooser.askcolor()
        if(selected_colour[1]!=None):
                self.fill_col=selected_colour[1]
                self.fs_colour_button.configure(bg=self.fill_col)                 
    def save_canvas(self):
        file_path = filedialog.asksaveasfilename(defaultextension="jpg")
        x=self.canvas.winfo_rootx()
        y=self.canvas.winfo_rooty()
        if(file_path):
                img=ImageGrab.grab(bbox=(x,y,x+1370,y+740))
                imgshow=messagebox.askyesno("Paint App","Do you want to see image")
                print(imgshow)
                if(imgshow):
                  img.show()
                  img.save(file_path)
    def load_canvas(self):
        image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
        #if(image_path):
           #img=Image.open(file=file_path)
        self.image = Image.open(image_path)
        self.imag= ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.imag)
    def clear_canvas(self):
        self.canvas.delete("all")
    def zoomIn(self): 
        scale=1.03
        self.canvas.scale(ALL, 0, 0, scale, scale)
        pass
    def zoomOut(self):
        scale=0.9
        self.canvas.scale(ALL, 0, 0, scale, scale)
        pass
    def brush_draw(self,event):
        if(self.last_x==None):
            self.last_x,self.last_y=event.x,event.y
            return
        self.canvas.create_line(self.last_x,self.last_y,event.x,event.y,width=self.width,capstyle="round",fill=self.b_colour)
        self.last_x,self.last_y=event.x,event.y
    def run(self,event=None):
        self.screen.mainloop()
    def cut_(self,event):
        if(self.cut_done==FALSE):
            self.last_x=event.x
            self.last_y=event.y
            self.remove_ids = self.canvas.find_overlapping(self.last_x, self.last_y,self.last_x+1,self.last_x+1)
            size=len(self.remove_ids)
            if(self.remove_ids==()):
                self.last_x=self.last_y=NONE
                return
            if(size==1):
                self.remov_id=self.remove_ids
            if(size>1):
                  self.remov_id=self.remove_ids[0]
                  pass
            self.cut_done=TRUE
            pass
        else:
            x=event.x
            y=event.y
            self.canvas.move(self.remov_id,x-self.last_x,y-self.last_y)
            self.last_x=self.last_y=NONE
            self.cut_done=FALSE
    def cut_section_notUsed(self,event):
        if(self.cut_done!=None):
            if(self.last_x==None):
                self.last_x=event.x
                self.last_y=event.y
                pass
            #image cut
            #remove that peace of image
            self.cut_done=TRUE
            self.last_x=self.last_y=None
    def paste_notUsed(self,event):
         #just paste
         x=event.x,event.y
         #paste image at x,y
         self.cut_done=FALSE
         pass
    def eraser(self,event):
        x=event.x
        y=event.y
        self.canvas.create_rectangle( x+self.eraser_width,y-self.eraser_width,x-self.eraser_width,self.eraser_width+y,outline=self.eraser_col,fill=self.eraser_col)
        pass
    def Points_curve(self,event):
        points=(event.x,event.y)
        self.point_used.append(points)
        print(points)
        if(len(self.point_used)==4):
            #draw curve
            drawn=TRUE
            p=self.point_used
            stx=self.point_used[0][0]
            sty=self.point_used[0][1]
            n=50
            for i in range(50):
                t=i/n
                x = (p[0][0] * (1-t)**3 + p[1][0] * 3 * t * (1-t)**2 + p[2][0] * 3 * t**2 * (1-t) + p[3][0] * t**3)
                y = (p[0][1] * (1-t)**3 + p[1][1] * 3 * t * (1-t)**2 + p[2][1] * 3 * t**2 * (1-t) + p[3][1] * t**3)
                self.canvas.create_line(x, y, stx, sty,fill=self.b_colour)
                stx=x
                sty=y
            self.point_used = []
PaintBrush (1350,740,"Apka Apna Paint").run()