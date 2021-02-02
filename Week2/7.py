import math


def ball_collide(ball1, ball2):
    ball1X, ball1Y, ball1R = ball1
    ball2X, ball2Y, ball2R = ball2
    if math.sqrt((ball1X - ball2X) ** 2 + (ball1Y - ball2Y) ** 2) < ball1R + ball2R:
        return True
    else:
        return False


if __name__ == '__main__':
    x1, y1, z1 = map(int, input().split())
    x2, y2, z2 = map(int, input().split())
    ball1 = (x1, y1, z1)
    ball2 = (x2, y2, z2)

    print("Ball Colliding :", ball_collide(ball1, ball2))