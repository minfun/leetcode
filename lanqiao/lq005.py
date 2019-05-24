import turtle as tl


def draw_smalltree(tree_length, tree_angle):
    if tree_length > 36:
        tl.forward(tree_length)
        tl.right(tree_angle)
        draw_smalltree(tree_length - 6, tree_angle)

        tl.left(2 * tree_angle)
        draw_smalltree(tree_length - 6, tree_angle)

        tl.rt(tree_angle)
        # if tree_length <= 30:
        tl.pencolor('green')
        # if tree_length > 30:
        tl.pencolor('brown')
        tl.backward(tree_length)


def main():
    tl.penup()
    tl.left(70)
    tl.backward(250)
    tl.pendown()
    tree_length = 60
    tree_angle = 20
    draw_smalltree(tree_length, tree_angle)
    tl.left(40)
    draw_smalltree(tree_length, tree_angle)
    tl.exitonclick()


if __name__ == '__main__':
    main()
