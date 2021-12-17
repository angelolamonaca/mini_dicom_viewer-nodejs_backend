module.exports = (sequelize, DataTypes) => {
  const Study = sequelize.define(
      'Study',
      {
        idPatient: DataTypes.INTEGER,
        studyName: DataTypes.STRING,
      },
      {
        defaultScope: {
          rawAttributes: { exclude: ['password'] },
        },
      },
  );
  Study.associate = function (models) {
    // associations can be defined here
    Study.belongsTo(models.Patient, { foreignKey: 'idPatient', as: 'patient' });
    Study.hasMany(models.Series, { foreignKey: 'idStudy', as: 'series', onUpdate: 'cascade', onDelete: 'cascade' });
    Study.hasMany(models.File, { foreignKey: 'idStudy', as: 'files', onUpdate: 'cascade', onDelete: 'cascade' });
  };
  return Study;
};