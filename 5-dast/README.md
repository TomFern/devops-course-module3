# Module 4 - DAST

**Goal**: Run DAST against the application.

## Steps

1. Install wapiti3: `pip install wapiti`
2. Start the application: `gunicorn -b 0:0:0:0:4000 app:app --daemon`
3. Run wapiti against the running application: `wapiti -u http://localhost:4000 -f html`
4. The generated report is located on `/root/.wapiti/generated_report`. Save the folder as an artifact for review

## Tip

- We are running black-box testing, so the application must be running before running wapiti
