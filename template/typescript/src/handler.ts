import { Request, Response } from 'express';

export default function(req: Request, res: Response): void {
  if (typeof(req.body) === 'string') {
    res.send(req.body.toUpperCase());
  } else {
    res.json(req.body);
  }
}
