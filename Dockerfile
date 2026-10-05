FROM python:3.12-slim AS build

ARG PUBLISH_DRAFT=''

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir .
RUN if [ -n "${PUBLISH_DRAFT}" ]; then pinoutxyz boards publish "${PUBLISH_DRAFT}"; fi
RUN python3 -m pinoutxyz build --site --minify

FROM nginxinc/nginx-unprivileged:alpine

COPY --from=build /app/output/site /usr/share/nginx/html

EXPOSE 8080
