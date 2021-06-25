## 무엇인가요?
웹 기반 신선한 식료품을 구매할 수 있는 플렛폼 **'Market Kurly'를 모티브로 핵심기능을 구현**한 프로젝트입니다.

## 프로젝트 구조
```
├── orders
├── products
├── users
├── marketkurly
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .gitignore
├── manage.py
├── requirements.txt
├── my_settings.py
```
* `orders`: 주문하기코드와 장바구니코드가 연관된 API입니다. 
	* `Cart` : 주문하기와 장바구니 기능입니다. 장바구니에 이미 상품이 있으면 새로운 주문하기 페이지를 생성하지 않게 만들었습니다.
* `products` : 상품과 연관된 API입니다.
    * `ProductList`   : 상품의 리스트 기능입니다. 상품의 리스트에 나오는 내용을 list 형식으로 정리했습니다.
    * `ProductDetail` : 상품의 디테일 기능입니다. 원하는 상품을 클릭했을 때 나오는 상세한 내용들을 list 형식으로 정리했습니다.
* `user` : 유저와 연관된 API입니다.
    * `Signup` : 회원가입 기능입니다. 비밀번호 길이, 이메일 유무 등 회원가입의 조건을 추가하여 만들었습니다.
    * `Signin` : 로그인 기능입니다. 비밀번호는 암호화를 시켜 데이터를 관리하고, 웹토큰을 발행하여 능률적인 접근 권한 관리를 할 수 있도록 만들었습니다.
* `.gitignore` : 보안이 필요한 개인정보 등 데이터를 모아두었습니다. 보안이 필요하기 때문에 숨김처리를 하였고, 따로 배포가 되지 않게 하였습니다. 
* `requirements.txt` : 개발 및 배포에 필요한 라이브러리를 정리했습니다.

## ERD 
URL : https://aquerytool.com:443/aquerymain/index/?rurl=d5e57212-86e1-4877-9ccb-232d2677a11e

비밀번호 : jznuti


## 어디서 볼 수 있나요?
소스 코드는 현재 GitHub에서 호스팅됩니다 : https://github.com/LEE-JUN-HA

## Reference
- 이 프로젝트는 오늘의 집 사이트를 참조하여 학습목적으로 만들었습니다. 
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
