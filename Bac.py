import turtle

# Mở hình ảnh và lấy thông tin kích thước
img = Image.open("Image.jpeg")
width, height = img.size

# Khởi tạo turtle
t = turtle.Turtle()
t.speed(0)  # Tốc độ vẽ nhanh nhất

# Vẽ từng pixel (đơn giản hóa)
for y in range(height):
    for x in range(width):
        pixel_color = img.getpixel((x, y))
        t.pencolor(pixel_color)  # Đặt màu bút
        t.forward(1)
        t.penup()
        t.forward(1)
        t.pendown()
    t.penup()
    t.goto(0, -y-1)  # Quay lại đầu dòng tiếp theo
    t.pendown()

turtle.done()
