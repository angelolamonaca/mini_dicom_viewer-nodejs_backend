require('dotenv').config();

module.exports = {
  development: {
    username: 'root',
    password: 'angelo_lamonaca',
    database: 'dicom-viewer',
    host: '127.0.0.1',
    port: '3308',
    dialect: 'mysql',
  },
};