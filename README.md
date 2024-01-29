# emotion.py 파일 설명

이 코드는 Hugging Face의 감정 분석 모델 (EmoBERTa-Large)을 사용하여 주어진 텍스트에 대한 감정을 추론하는 간단한 함수를 구현한 것입니다.

API_URL 변수에는 Hugging Face 모델 인퍼런스 API의 엔드포인트 URL이 저장되어 있습니다.
headers 변수에는 Hugging Face 모델 인퍼런스 API에 요청할 때 필요한 인증 토큰이 저장되어 있습니다.
query 함수는 주어진 텍스트 데이터를 인자로 받아, 해당 데이터를 Hugging Face 모델 API로 전송하고, 그에 대한 응답을 JSON 형식으로 반환합니다.
requests.post를 사용하여 POST 요청을 보내고, 요청 헤더에는 headers 변수에 저장된 인증 토큰이 포함되어 있습니다.
함수는 API 응답을 JSON 형식으로 파싱하여 반환합니다.
실제 텍스트 데이터로 data 변수에 있는 어떠한 문장을 사용하여 query 함수를 호출하고, 그 결과를 data 변수에 저장합니다.

코드 설명
round_recursive로 입력값 item을 받고,
item이 정수/소수인 경우 해당 숫자값을 100곱하고 소수점 둘쨰짜리까지 표시하게 한다.
zfill(5) 메서드로 문자열의 길이를 5로 만들어 주고, 앞에 부족한 자릿수를 0으로 채운다.
