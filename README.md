# Satspay Session

This micro app delivers a custom Invoice amount from the SatsPayExtension fron LNbits via an Flask API endpoint. 
Why do this? Because we want to be able to specify a lightning invoice in sats with the USD amount (or any other fiat equivalent amount) with a link instead of creating it manually from within the LNBits web interface. 

Example: http://satspaysession.vercel.com/usd?amount=100 

The above link, given the parameters of 100 USD, will calculate the equivalent amount of sats and 
then redirect the user to a lightning invoice created by the satspayserver extension.


[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Fflask&demo-title=Flask%20%2B%20Vercel&demo-description=Use%20Flask%202%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fflask-python-template.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994156/random/flask.png)

# Flask + Vercel

This example shows how to use Flask 2 on Vercel with Serverless Functions using the [Python Runtime](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python).

## Demo

https://flask-python-template.vercel.app/

## How it Works

This example uses the Web Server Gateway Interface (WSGI) with Flask to enable handling requests on Vercel with Serverless Functions.

## Running Locally

```bash
npm i -g vercel
vercel dev
```

Your Flask application is now available at `http://localhost:3000`.

## One-Click Deploy

Deploy the example using [Vercel](https://vercel.com?utm_source=github&utm_medium=readme&utm_campaign=vercel-examples):

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Fflask&demo-title=Flask%20%2B%20Vercel&demo-description=Use%20Flask%202%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fflask-python-template.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994156/random/flask.png)
