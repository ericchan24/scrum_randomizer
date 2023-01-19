FROM python:3.10-slim
LABEL org.opencontainers.image.authors="echan@nfa.futures.org"
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN mkdir ~/.streamlit  
COPY .streamlit/config.toml ~/.streamlit/config.toml
RUN pip install -r requirements.txt
EXPOSE 80
COPY . /app     
ENTRYPOINT ["streamlit", "run"]
CMD ["01_🏠_Home.py"]