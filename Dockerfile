FROM python:3.7
WORKDIR /app

# Copy the requirements.txt file and install all dependencies.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Downloading and installing gcloud package.
RUN curl https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz > /tmp/google-cloud-sdk.tar.gz
RUN mkdir -p /usr/local/gcloud \
  && tar -C /usr/local/gcloud -xvf /tmp/google-cloud-sdk.tar.gz \
  && /usr/local/gcloud/google-cloud-sdk/install.sh
ENV PATH $PATH:/usr/local/gcloud/google-cloud-sdk/bin

# Test dependencies.
RUN gcloud -v
RUN behave --version

# Copy project files (see .dockerignore).
COPY . .

# Run the tests.
ENTRYPOINT ["/app/execute.sh"]