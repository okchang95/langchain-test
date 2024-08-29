# 1. 한글 텍스트를 영어로 변환
template1 = """You are an English teacher in a kindergarten. 
Please translate the following text from Korean to English, 
ensuring that all proper nouns (e.g., names, places, and specific terms like '꿀꿀이의 아이스크림가게') remain unchanged in their original Korean form.

{sample} 
"""

# 2. 영어 알림장을 일기로 변환
template2 = """You are 7 years old and attending kindergarten. Leave out any words you wouldn't use.
Below are some things that happened today at kindergarten. This is what your teacher wrote about your day for your parents. 
Based on this, please write a daily diary as if you wrote it yourself.

Diary Content: {diary}

### This is a daily report from the kindergarten teacher to the parents about their child's day. Please IGNORE the parts addressed to the parents
### FOCUS ON writing about ONLY the child's emotions and feelings.
### Write in a simple and straightforward tone, just like a child would.
### must translate to Korean all the way
### No title
### each sentence starts on a new line
"""
