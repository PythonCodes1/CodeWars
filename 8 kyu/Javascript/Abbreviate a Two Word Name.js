// Abreviating the first and last name of a person separated by a period
// 8 kyu

const abbrevName = name =>
  name
    .split(' ')
    .map(name => name[0].toUpperCase())
    .join('.')

// Function Export
module.exports = abbrevName
