# 1. 한글 텍스트를 영어로 변환
# + 이름 정보 삭제(08/30)
template1 = """You are an English teacher in a kindergarten. 
Please translate the following text from Korean to English, 
ensuring that all proper nouns (e.g., names, places, and specific terms like '꿀꿀이의 아이스크림가게') remain unchanged in their original Korean form.
Additionally, please remove any person’s name included in the input text.

{sample} 
"""

# 2. 영어 알림장을 일기로 변환
# + 어색한 부분 수정 예시 전달(8/30)
# + 기분상태 파악(8/30)
template2 = """You are 7 years old and attending kindergarten. Leave out any words you(7's child) wouldn't use.
Below are some things that happened today at kindergarten. This is what your teacher wrote about your day for your parents. 

Based on this, please write a daily diary as if you wrote it yourself.
Based on the context, identify the child's emotional state for the day (e.g., happy, sad, excited, scared) and write the diary entry in a way that reflects the child's emotions."
Additionally, when rewriting the text as if a child wrote it, make sure to use simple and natural expressions. For example, instead of "내 웃음소리가 계속 들렸어요," write "재밌었어요."

Diary Content: {diary}

### This is a daily report from the kindergarten teacher to the parents about their child's day. Please IGNORE the parts addressed to the parents. For example, instead of "공휴일은 잘 보내셨나요?," write ""
### FOCUS ON writing about ONLY the child's emotions and feelings.
### Write in a simple and straightforward tone, just like a child would.
### must translate to Korean all the way
### No title
### each sentence starts on a new line
"""

# 0830 ####################################

"""Please translate the following text and remove any person’s name included in the input text. 
"""


# 3. 영어로 변환된 텍스트를 요약
template3 = """You are an English teacher in a kindergarten. 
Please translate the following text from Korean to English, 
ensuring that all proper nouns (e.g., names, places, and specific terms like '꿀꿀이의 아이스크림가게') remain unchanged in their original Korean form.

{sample} 
"""

# 4. 요약된 내용을 바탕으로 일기 작성
template4 = """

"""
