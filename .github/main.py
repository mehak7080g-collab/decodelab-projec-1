name: Run VEX

on:
  workflow_dispatch:
  push:
    branches:
      - main

jobs:
  run-vex:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Run main.py
        run: |
          python main.py
