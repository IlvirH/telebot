FROM python:slim
ENV TOKEN='TOKEN'
COPY . . 
RUN pip install -r req.txt
CMD python bot.py
