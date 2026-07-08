# Compose healthcheck patterns

## HTTP service

```yaml
healthcheck:
  test: ["CMD", "curl", "-fsS", "http://localhost:8080/health"]
  interval: 30s
  timeout: 5s
  retries: 3
  start_period: 30s
```

Use only when `curl` exists in the image. Prefer a native application health command when available.

## PostgreSQL

```yaml
healthcheck:
  test: ["CMD-SHELL", "pg_isready -U $${POSTGRES_USER} -d $${POSTGRES_DB}"]
  interval: 10s
  timeout: 5s
  retries: 5
  start_period: 30s
```

## Redis

```yaml
healthcheck:
  test: ["CMD", "redis-cli", "ping"]
  interval: 10s
  timeout: 3s
  retries: 5
```

## Readiness dependency

```yaml
depends_on:
  db:
    condition: service_healthy
```

This gates dependent creation/startup. It does not continuously restart the dependent if the dependency later becomes unhealthy.

## Timing

Approximate worst-case detection after startup grace as `interval × retries + timeout`, while accounting for runtime scheduling behavior. Choose values from service objectives rather than copying examples unchanged.
