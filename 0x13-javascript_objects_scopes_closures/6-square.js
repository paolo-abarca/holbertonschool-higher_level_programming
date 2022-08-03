#!/usr/bin/node
class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      let row = '';

      for (let j = 0; j < this.width; j++) {
        row = row + c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
