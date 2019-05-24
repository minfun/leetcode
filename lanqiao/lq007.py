import turtle


def main ():
    i = 1
    # turtle.begin_fill()
    while i <= 5:
        turtle.forward(150)
        turtle.right(72)
        i = i+1
    # turtle.end_fill()


if __name__ == "__main__":
    for i in range(8):
        turtle.right(45)
        main()
    turtle.exitonclick()
