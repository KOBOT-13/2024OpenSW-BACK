import os
from openai import OpenAI

api_key = "API_KEY"
os.environ["OPENAI_API_KEY"] = api_key

client = OpenAI()
character_key = 1

character_map = {
    0: "답변은 한국어로 하고 백설공주의 마녀의 입장에서 대답해줘",
    1: "답변은 한국어로 하고 토끼와 거북이의 토끼의 입장에서 대답해줘",
    2: "답변은 한국어로 하고 토끼와 거북이의 거북이의 입장에서 대답해줘",
    3: "답변은 한국어로 하고 아기돼지 삼형제의 첫째돼지의 입장에서 대답해줘",
    4: "답변은 한국어로 하고 아기돼지 삼형제의 둘째돼지의 입장에서 대답해줘",
    5: "답변은 한국어로 하고 아기돼지 삼형제의 셋째돼지의 입장에서 대답해줘"
}

# character_key에 해당하는 characters를 설정
characters = character_map[character_key]

    
# 챗봇 함수 정의

def chatbot(input_message):
    try:
        
        model = "gpt-3.5-turbo"
       
        messages = [
                {   "role":"system",
                     "content": characters
                     },
                {
                    "role": "user",
                    "content": input_message,
                }
            ]
        

        # OpenAI API 호출
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0
        )

        # 응답 메시지 추출
        if response.choices:
            bot_response = response.choices[0].message.content
        else:
            bot_response = "No response from the model"

        return bot_response

    except Exception as e:
        return f"Error: {str(e)}"

# 메인 함수 (챗봇 실행)
if __name__ == "__main__":
    print("챗봇을 시작합니다. 종료하려면 '그만'이라고 입력하세요.")
    
    while True:
        user_input = input("사용자: ")

        # 종료 조건 설정 --> (프론트에서 창을 나가면 받는 값으로 설정해주면 될 듯 합니다.~)
        if user_input.lower() == '그만':
            print("챗봇을 종료합니다.")
            break

        # 챗봇 함수 호출 및 응답 출력
        bot_response = chatbot(user_input)
        print(f"챗봇: {bot_response}")
