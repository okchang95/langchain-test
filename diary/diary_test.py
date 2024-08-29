from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from langchain_teddynote import logging
from dotenv import load_dotenv

import json
import os
import sys
from tqdm import tqdm
from prompt_templates import template1, template2

load_dotenv()  # API KEY 정보로드
logging.langsmith("langsmith-test-0829")  # 프로젝트 이름 입력

# if len(sys.argv) < 2:
#     print("사용법: python script_name.py <filename>")
#     sys.exit(1)

# inputfilename = sys.argv[1]
# input_file = f"{inputfilename}"

files = os.listdir("samples")
for input_file in tqdm(
    files,
    desc="Processing files",
):
    print(f"{input_file} is in progress........")
    with open("data.json", "r", encoding="utf-8") as f:
        samples = json.load(f)
    input_sample = samples[input_file]

    model1 = ChatOpenAI(
        model="gpt-4o-mini",
        max_tokens=2048,
        temperature=0.2,
    )

    model2 = ChatOpenAI(
        model="gpt-4o-mini",
        max_tokens=2048,
        temperature=0.2,
    )

    prompt1 = PromptTemplate.from_template(template1)
    output_parser1 = StrOutputParser()
    chain1 = prompt1 | model1 | output_parser1

    prompt2 = PromptTemplate.from_template(template2)
    output_parser2 = StrOutputParser()
    chain2 = prompt2 | model2 | output_parser2

    translated = chain1.invoke({"sample": input_sample})
    result = chain2.invoke({"diary": translated})

    with open(
        f"results/{input_file.split('.')[0]}_result.txt", "w", encoding="utf-8"
    ) as f:
        f.write(result)
    # print()
    # print(f"==========================INPUT==========================")
    # print(input_sample)
    # print()
    # print(f"==========================OUTPUT==========================")
    # print(result)

# for token in chain.stream({"diary": translated}):
#     # 스트림에서 받은 데이터의 내용을 출력합니다. 줄바꿈 없이 이어서 출력하고, 버퍼를 즉시 비웁니다.
#     print(token, end="", flush=True)
