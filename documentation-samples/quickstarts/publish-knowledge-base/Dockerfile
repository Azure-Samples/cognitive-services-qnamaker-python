# BUILD IMAGE
# $ docker build --no-cache -t qnamaker-py3-publish .
#
# RUN CODE
#
# WINDOWS BASH COMMAND 
# $ winpty docker run -it --rm --name qnamaker-py3-publish publish
#
# NON-WINDOWS
# $ docker run -it --rm --name qnamaker-py3-publish publish

FROM python:3

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "./publish-kb-3x.py" ]