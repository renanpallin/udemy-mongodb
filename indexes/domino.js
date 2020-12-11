function domino() {
  for (let x = 0; x <= 6; x++) {
    for (let y = 0; y <= x; y++) {
      db.domino.insert({
        piece: [x, y],
      });
    }
  }
}
