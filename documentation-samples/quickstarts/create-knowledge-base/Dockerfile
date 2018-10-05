# BUILD IMAGE
# $ docker build --no-cache -t qnamaker-py3-create-kb .
#
# RUN CODE
#
# WINDOWS BASH COMMAND 
# $ winpty docker run -it --rm --name qnamaker-py3-create-kb qnamaker-py3-create-kb
#
# NON-WINDOWS
# $ docker run -it --rm --name qnamaker-py3-create-kb qnamaker-py3-create-kb

FROM python:3

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "./create-new-knowledge-base-3x.py" ]