const fs = require('fs');

const jsonData = fs.readFileSync('data.json', 'utf8');

const regions = JSON.parse(jsonData)['Regions'];

const endpoints = regions.map(r => (r['Endpoint']));

console.log(endpoints);