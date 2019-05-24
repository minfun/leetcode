import turtle


def draw_branch(branch_length):
    if branch_length > 5:
        turtle.forward(branch_length)

        # 绘制右侧树枝
        turtle.right(20)
        draw_branch(branch_length - 15)

        # 绘制左侧树枝
        turtle.left(40)
        draw_branch(branch_length - 15)

        # 返回之前的树枝
        turtle.right(20)
        turtle.backward(branch_length)


if __name__ == '__main__':
    turtle.left(90)
    draw_branch(80)
    turtle.exitonclick()
