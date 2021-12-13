require('dotenv').config();

module.exports = {
  development: {
    username: 'root',
    password: 'angelo_lamonaca',
    database: 'dicom-viewer',
    host: '127.0.0.1',
    dialect: 'mysql',
    use_env_variable: 'jdbc:mysql://localhost:3308/dicom-viewer',
  },
};