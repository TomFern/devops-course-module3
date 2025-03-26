# Module 6 - Configure tests in the CI pipeline

**Goal**: Use shift-left security on the CI pipeline

## Steps

1. Setup a pipeline that run the tests. Refer to pipeline.png for an example of a pipeline that runs the tests.
2. Bonus points if you can fix the errors and get the pipeline into a green state

## Tips

- On the pipeline use the container image: `registry.semaphoreci.com/python:3.12.1`
- Check pipeline.png in this folder to see an example.
- The `solution` branch contains a working pipeline
- If an audit/scanning tools is causing the pipeline to stop, you can append `|| true` to the end of the failing command so the pipeline doesn't fail. Use this only for debugging purposes.
