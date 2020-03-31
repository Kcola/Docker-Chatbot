FROM joyzoursky/python-chromedriver:3.7
COPY . /usr/workspace
RUN pip install selenium flask flask_cors
CMD python /usr/workspace/server.py