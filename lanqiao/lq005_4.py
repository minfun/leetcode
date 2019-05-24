import turtle


def draw_branch(branch_length):
    if branch_length > 36:
        turtle.forward(branch_length)

        # 绘制右侧树枝
        turtle.right(10)
        draw_branch(branch_length - 6)

        # 绘制左侧树枝
        turtle.left(20)
        draw_branch(branch_length - 6)

        # 返回之前的树枝
        turtle.right(10)
        turtle.backward(branch_length)


if __name__ == '__main__':
    turtle.left(90)
    draw_branch(60)
    turtle.exitonclick()
