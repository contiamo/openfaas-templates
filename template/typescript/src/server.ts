import * as bodyParser from 'body-parser';
import * as compression from 'compression';
import * as express from 'express';
import * as logger from 'morgan';

import handler from './handler';

class Server {

  public app: express.Application;

  constructor() {
    this.app = express();
    this.config();
  }

  public config(): void {
    // express middleware
    this.app.use(bodyParser.urlencoded({extended: true}));
    this.app.use(bodyParser.json({type: 'application/json'}));
    this.app.use(bodyParser.text({type: '*/*'}));
    this.app.use(logger('dev'));
    this.app.use(compression());

    // handler
    this.app.all('/', handler);
  }

}

// export
export default new Server().app;
