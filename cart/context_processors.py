from .cart import Cart


def cart(request):

    # 세션 확인 테스트
    # Cart.decrypt_all_sessions()
    print("카트 함수 호출")

    # 카트 객체를 생성해서 딕셔너리 형태로 리턴
    return {"cart": Cart(request)}
