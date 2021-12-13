module.exports = (sequelize, DataTypes) => {
  const Patient = sequelize.define(
      'Patient',
      {
        idPatient: DataTypes.INTEGER,
        name: DataTypes.STRING,
      },
      {
        defaultScope: {
          rawAttributes: { exclude: ['password'] },
        },
      },
  );
  Patient.associate = function (models) {
    // associations can be defined here
    Patient.hasMany(models.Study, { foreignKey: 'idPatient', as: 'studies' });
    Patient.hasMany(models.Series, { foreignKey: 'idPatient', as: 'series' });
    Patient.hasMany(models.File, { foreignKey: 'idPatient', as: 'files' });
  };
  return Patient;
};