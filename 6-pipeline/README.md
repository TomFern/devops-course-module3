# Module 6 - Configure tests in the CI pipeline

**Goal**: Use shift-left security on the CI pipeline

## Steps

1. Setup a pipeline that run the tests. Refer to pipeline.png for an example of a pipeline that runs the tests.
2. Fix the errors revealed until the pipeline is green.

## Tips

- On the pipeline use the container image: `registry.semaphoreci.com/python:3.12.1`
- Check pipeline.png in this folder to see an example.
- If you have trouble running `app.py` in CI try using `nohup python app.py &`
