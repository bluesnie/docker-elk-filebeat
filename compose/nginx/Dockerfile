FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
COPY ./config/nginx.conf /etc/nginx/conf.d

# 关闭守护模式
CMD ["nginx", "-g", "daemon off;"]