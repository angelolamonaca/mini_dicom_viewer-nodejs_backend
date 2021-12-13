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
    Patient.hasMany(models.Study, { foreignKey: 'id', as: 'studies' });
    Patient.hasMany(models.Series, { foreignKey: 'id', as: 'series' });
    Patient.hasMany(models.File, { foreignKey: 'id', as: 'files' });
  };
  return Patient;
};