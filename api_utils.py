import openai

# 设置 API 密钥
openai.api_key = "请替换成api"
openai.base_url = "https://free.gpt.ge/v1/"
openai.default_headers = {"x-foo": "true"}

def translate_text(direction, style, input_text):
    try:
        # 设置API请求的prompt，根据选择的风格调整
        if direction == "英译中":
            target_language = "Chinese"
        elif direction == "中译英":
            target_language = "English"
        elif direction == "中译日":
            target_language = "Japanese"
        elif direction == "日译中":
            target_language = "Chinese"

        if style == "学术风格":
            style_prompt = "in an academic style"
        elif style == "地道表达":
            style_prompt = "in a natural, colloquial style"
        elif style == "正式语气":
            style_prompt = "in a formal tone"
        elif style == "非正式语气":
            style_prompt = "in an informal tone"

        # 修改prompt以仅返回翻译结果
        prompt = f"Translate the following text to {target_language} {style_prompt}, and only provide the translation: {input_text}"
        
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )
        # 直接获取并返回翻译结果
        translation = response.choices[0].message.content.strip()
        return translation
    except Exception as e:
        return f"调用API时出错：{str(e)}"
