function populatePeople() {
  const firstNames = [
    'Renan',
    'Luan',
    'Letícia',
    'João',
    'Lucas',
    'Luiz',
    'Daniel',
    'Eduardo',
    'Gisele',
    'Rodrigo',
    'José',
    'Antônio',
    'Marcos',
    'Gabriel',
    'Rafael',
    'Marcelo',
    'Daniel',
    'Bruno',
    'Carlos',
    'Roberto',
  ];

  const lastNames = [
    'Pallin',
    'Souza',
    'Rocha',
    'Crato',
    'Silva',
    'Santos',
    'Oliveira',
    'Lima',
    'Pereira',
    'Ferreira',
    'Costa',
    'Rodrigues',
    'Almeida',
    'Nascimento',
    'Alves',
    'Cavalho',
    'Araújo',
    'Ribeiro',
    'Barbosa',
    'Barros',
  ];

  function _randomInt(start = 0, end = 100) {
    return Math.floor(Math.random() * (start - end) + end);
  }

  const labDb = db.getSiblingDB('lab');

  let _id = 0;
  while (_id++ < 1e8) {
    const name =
      firstNames[_randomInt(0, firstNames.length - 1)] +
      ' ' +
      lastNames[_randomInt(0, lastNames.length - 1)];

    labDb.people.insert({
      _id,
      name,
      age: _randomInt(12, 120),
      height: _randomInt(140, 210),
    });

    if (_id % 1e4 === 0) print(`Inserimos ${_id} documentos...`);
  }
  print('Prontinho! 100 MILHÕES de documentos inseridos!');
}
