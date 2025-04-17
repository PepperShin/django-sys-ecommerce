from django.test import TestCase
import pickle

# Create your tests here.


# dev_28 시리얼라이제이션의 이해
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


class ObjectAPITest(TestCase):
    def setUp(self):
        pass

    def test_path(self):
        dict = {
            "add": add,
            "sub": sub,
        }
        url = "add"
        print(dict[url](1, 2))
        print(dict["sub"](2, 1))

    # 사각형 rect 객체를 직렬화 (Serialization)
    def test_serialization(self):
        rect = Rectangle(10, 20)

        with open(
            "rect.data", "wb"
        ) as f:  # open은 rect.data 를 열어서 wb(write binary)로 저장한다.
            pickle.dump(
                rect, f
            )  # pickel이 직렬화 함수. rect 클래스 객체를 f에 직렬화 하여 저장(바이너리)

        # 역직렬화 (Deserialization)
        with open("rect.data", "rb") as f:
            r = pickle.load(f)

        print(r.width, r.height)
