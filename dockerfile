FROM python:slim
ENV TOKEN='6040282735:AAH2ZNu_1bIyWV5zu-t2dhZXvinZco77pwE'
COPY . . 
RUN pip install -r req.txt
CMD python bot.py