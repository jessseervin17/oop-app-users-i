#!/usr/bin/env bash

# Exit immediately if any command fails (so CI sees a failure)
set -e

cd "$(dirname "$0")"

IMAGE_NAME="pytest-app-users"

echo "----------------------------------------"
echo "Building Docker image: $IMAGE_NAME..."
echo "----------------------------------------"
docker build -t "$IMAGE_NAME" -f Dockerfile.test .

echo "----------------------------------------"
echo "Running containerized tests..."
echo "----------------------------------------"
docker run --rm "$IMAGE_NAME"

echo "----------------------------------------"
echo "Done! Tests passed."
echo "----------------------------------------"