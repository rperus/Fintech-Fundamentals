FROM debian:stretch

USER root

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion

RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-2019.07-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

RUN apt-get install -y build-essential libssl-dev libffi-dev python-dev
RUN apt-get install -y libgmp-dev
RUN apt-get install -y libmpfr-dev
RUN apt-get install -y libmpc-dev

# Install JupyterLab
RUN apt-get install python3-pip -y
RUN pip3 install --upgrade pip setuptools

RUN apt-get install -y build-essential libssl-dev libffi-dev python-dev
RUN apt-get install -y libgmp-dev
RUN apt-get install -y libmpfr-dev
RUN apt-get install -y libmpc-dev

RUN apt-get install -y python-pip python-dev

# Install JupyterLab
RUN pip3 install jupyterlab && jupyter serverextension enable --py jupyterlab

WORKDIR "/root/"

# install postgres to connect using CLI
RUN apt-get install postgresql -y

# run
EXPOSE 8888

# can change the --NotebookApp.token to have better password/token
CMD jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token="secret_stuff"