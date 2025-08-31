FROM jupyterhub/jupyterhub:latest

RUN apt-get update && apt-get install -y \
    python3-pip \
    git \
    wget \
    bzip2 \
    && rm -rf /var/lib/apt/lists/*

# Install Miniconda (Python 3.8)
ENV CONDA_DIR=/opt/conda
ENV PATH=$CONDA_DIR/bin:$PATH
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-py311_24.1.2-0-Linux-x86_64.sh -O /tmp/miniconda.sh \
    && bash /tmp/miniconda.sh -b -p $CONDA_DIR \
    && rm /tmp/miniconda.sh \
    && $CONDA_DIR/bin/conda clean -afy

# Ensure conda is initialized
RUN $CONDA_DIR/bin/conda init bash

RUN pip install jupyterlab \
    && pip install jupyterhub-nativeauthenticator \
    && pip install jupyterlab-git

RUN mkdir -p /srv/jupyterhub/work && chmod 777 /srv/jupyterhub/work

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py

CMD ["jupyterhub", "-f", "/etc/jupyterhub/jupyterhub_config.py"]