# BUILD IMAGE
# $ docker build --no-cache -t qnamaker-py3-get-answer .
#
# RUN CODE
#
# WINDOWS BASH COMMAND 
# $ winpty docker run -it --rm --name qnamaker-py3-get-answer qnamaker-py3-get-answer
#
# NON-WINDOWS
# $ docker run -it --rm --name qnamaker-py3-get-answer qnamaker-py3-get-answer

FROM python:3

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "./get-answer-3x.py" ]