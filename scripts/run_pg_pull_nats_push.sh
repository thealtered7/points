#!/usr/bin/env bash

docker run --rm \
-e "PGPORT=${PGPORT}" \
-e "PGHOST=${PGHOST}" \
-e "PGUSER=${PGUSER}" \
-e "PGPASSWORD=${PGPASSWORD}" \
-e "PGDATABASE=${PGDATABASE}" \
-e "NATS_SERVERS=${NATS_SERVERS}" \
python-points:0.2  pg_pull_nats_push