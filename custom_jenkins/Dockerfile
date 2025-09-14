# Sử dụng Jenkins LTS làm base image
FROM jenkins/jenkins:lts

# Chuyển sang root để cài thêm công cụ
USER root

# Cài đặt Docker CLI và các gói cần thiết
RUN apt-get update && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] \
    https://download.docker.com/linux/debian $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list && \
    apt-get update && \
    apt-get install -y docker-ce-cli && \
    rm -rf /var/lib/apt/lists/*

# Đảm bảo jenkins home vẫn tồn tại
RUN mkdir -p /var/jenkins_home && chown -R root:root /var/jenkins_home

# Giữ Jenkins chạy bằng root để có quyền dùng docker socket
USER root

# Jenkins sẽ khởi động như mặc định
