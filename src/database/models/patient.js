module.exports = (sequelize, DataTypes) => {
  const Patient = sequelize.define(
      'Patient',
      {
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
    Patient.hasMany(models.Study, { foreignKey: 'idPatient', as: 'studies', onUpdate: 'cascade', onDelete: 'cascade' });
    Patient.hasMany(models.Series, { foreignKey: 'idPatient', as: 'series', onUpdate: 'cascade', onDelete: 'cascade' });
    Patient.hasMany(models.File, { foreignKey: 'idPatient', as: 'files', onUpdate: 'cascade', onDelete: 'cascade' });
  };
  return Patient;
};