FROM crux/python:onbuild

EXPOSE 1338/udp

ENTRYPOINT ["factory"]
CMD []
