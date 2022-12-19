FROM python:3.10

RUN mkdir -p /srv/stocks
RUN mkdir -p /data
RUN mkdir -p /docs

COPY data /data
COPY src /srv/stocks

#####
# Custom Section
RUN pip install pandas matplotlib numpy
RUN pip install cairosvg colorcet
RUN pip install requests
#####

WORKDIR /srv
ENTRYPOINT [ "python3" ]
CMD [ "-m", "stocks"]
