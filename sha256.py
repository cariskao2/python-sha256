name: workflow
on:
    workflow_dispatch:

jobs:

    pytest:
        runs-on: ubuntu-22.04
        steps:
            - name: checkout code
            uses: actions/checkout@v3
            - name: check default env
            run: env
            - name: print env
            run: echo $GITHUB_REPOSITORY
            # 這裡使用
