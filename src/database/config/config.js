require('dotenv').config();

module.exports = {
  development: {
    username: 'root',
    password: 'angelo_lamonaca',
    database: 'dicom-viewer',
    host: 'localhost',
    port: '3306',
    dialect: 'mysql',
  },
};