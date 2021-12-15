module.exports = (sequelize, DataTypes) => {
  const File = sequelize.define(
      'File',
      {
        idPatient: DataTypes.INTEGER,
        idStudy: DataTypes.INTEGER,
        idSeries: DataTypes.INTEGER,
        filePath: DataTypes.STRING,
      },
      {
        defaultScope: {
          rawAttributes: { exclude: ['password'] },
        },
      },
  );
  File.associate = function (models) {
    // associations can be defined here
    File.belongsTo(models.Patient, { foreignKey: 'idPatient', as: 'patient' });
    File.belongsTo(models.Patient, { foreignKey: 'idStudy', as: 'study' });
    File.belongsTo(models.Patient, { foreignKey: 'idSeries', as: 'series' });
  };
  return File;
};