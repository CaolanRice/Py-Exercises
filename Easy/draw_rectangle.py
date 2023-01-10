def drawRectangle(width, height):
    if width < 1 or height < 1:
        return
    for row in range(height):
        for column in range(width):
            print('#' * height, end="")
        print()


drawRectangle(10, 4)


# nested for loop vs string replication
# def rectangle(width, height):
#     for i in range(height):
#         print('#' * width)

# rectangle(10, 4)
