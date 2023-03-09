def get_vat(price, vat_rate = 0.1) :                        #vat_rate를 입력하지 않으면 0.1로 처리됨!
    return price * vat_rate                                 #return을 활용해 함수값을 정의하면 활용도가 높음!
print(get_vat(56000000, 0.5))
print(get_vat(100))