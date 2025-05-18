#!/bin/bash
echo "Starting ELK and Grafana stack..."
cd "$(dirname "$0")/../dashboard"
docker-compose up -d
