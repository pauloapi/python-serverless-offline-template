
# Serverless Offline Template

This project was generated with [Serverless CLI](https://github.com/serverless/serverless).


## Prerequisites 

Before you begin, make sure your development environment includes `Node.js®`, `Python3.6`, `virtualenv`, npm package manager and `Serverless`. 


### Node.js

Serverless requires `Node.js` version 6 or higher.

* To check your version, run `node -v` in a terminal/console window.

* To get `Node.js`, go to [nodejs.org](https://nodejs.org "Nodejs.org").


### Python

This Project requires `Python` version *3.6.X*.

* To check your version, run `python --version` in a terminal/console window.

* To get `Python3.6`, go to [python.org](https://www.python.org/downloads/release/python-360/ "Python 3.6.0").


### npm package manager

Serverless depend on features and functionality provided by libraries that are available as [npm packages](https://docs.npmjs.com/getting-started/what-is-npm). To download and install npm packages, you must have an npm package manager. 

This setup guide uses the [npm client](https://docs.npmjs.com/cli/install) command line interface, which is installed with `Node.js` by default. 

To check that you have the npm client installed, run `npm -v` in a terminal/console window.


### Serverless CLI

Install the Serverless CLI globally. 

To install the CLI using `npm`, open a terminal/console window and enter the following command:

`npm install -g serverless`


### Virtualenv

Install and use virtualenv

#Install virtualenv
`pip install virtualenv`

#Create virtualenv
`virtualenv env`

#unix: activate virtual environment
`. env/bin/activate`
#windows: activate virtual environment
`env\Scripts\activate`


### Gettings Started

Activate virtual environment and install python requirements 

`pip install -r requirements.txt`


## Development server

Activate virtual environment and run `npm run offline` for a dev server. Navigate to `http://localhost:3000/`. The app will automatically reload if you change any of the source files. To use other port, you may run `npm run offline -- --port 3001`.


## Further help

To get more help on the Serverless CLI use `serverless help` or go check out the [Serverless CLI Reference](https://serverless.com/framework/docs/providers/aws/cli-reference/).
