import turtle


def main ():
    i = 1
    turtle.begin_fill()
    while i <= 5:
        turtle.forward(50)
        turtle.right(144)
        i = i+1
    turtle.end_fill()
    turtle.exitonclick()


if __name__ == "__main__":
    main()
