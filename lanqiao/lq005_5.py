import turtle as tl


def draw_smalltree(tree_length, tree_angle):
    if tree_length > 36:
        tl.forward(tree_length)
        tl.right(tree_angle)
        draw_smalltree(tree_length - 6, tree_angle)

        tl.left(2 * tree_angle)
        draw_smalltree(tree_length - 6, tree_angle)

        tl.rt(tree_angle)
        tl.pencolor('green')
        tl.backward(tree_length)


def draw_tree():
    tl.penup()
    tl.left(20)
    tl.backward(250)
    tl.pendown()
    tree_length = 60
    tree_angle = 10
    draw_smalltree(tree_length, tree_angle)
    tl.left(20)
    draw_smalltree(tree_length, tree_angle)


def main():
    tl.screensize(800, 600, 'white')
    tl.penup()
    tl.pencolor('white')
    tl.setpos(300, 100)
    tl.pencolor('black')
    draw_tree()
    # tl.left(20)
    # tl.forward(250)
    # tl.reset()
    # draw_tree()
    # tl.reset()
    # tl.forward(250)
    # draw_tree()
    tl.setheading(0)
    tl.pencolor('white')
    tl.setpos(400, 200)
    tl.pencolor('black')
    draw_tree()

    tl.setheading(0)
    tl.pencolor('white')
    tl.setpos(100, -100)
    tl.pencolor('black')
    draw_tree()

    tl.exitonclick()


if __name__ == '__main__':
    main()
