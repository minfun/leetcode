import turtle

turtle.color('yellow')
turtle.bgcolor('red')


def drawFillStarByOffsetAndSize(offsetX, offsetY, size):
    def move(x, y):
        turtle.up()
        turtle.goto(x, y)
        turtle.down()

    def drawStar(starSize):
        for i in range(5):
            turtle.left(144)
            turtle.back(starSize)

    turtle.begin_fill()
    move(offsetX, offsetY)
    drawStar(size)
    turtle.end_fill()


drawFillStarByOffsetAndSize(-300, 150, 100)
drawFillStarByOffsetAndSize(-140, 250, 50)
drawFillStarByOffsetAndSize(-100, 180, 50)
drawFillStarByOffsetAndSize(-125, 100, 50)
drawFillStarByOffsetAndSize(-180, 30, 50)
turtle.done()
