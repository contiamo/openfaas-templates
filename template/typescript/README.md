Basic typescript function template
==================================

## Scope

This is a template to create an simple openfaas function using typescript and nodejs.

Unlike other templates this doesn't require the watchdog binary and will not spawn a fresh node instance for every request.

Have fun!

## Usage

Just edit `src/handler.ts` and rebuild the docker image using `docker build -t my-function-name .`


