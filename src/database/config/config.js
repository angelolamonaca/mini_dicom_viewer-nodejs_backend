require('dotenv').config();

module.exports = {
  development: {
    username: 'root',
    password: 'angelo_lamonaca',
    database: 'dicom-viewer',
    host: '172.17.0.1',
    port: '3306',
    dialect: 'mysql',
  },
};