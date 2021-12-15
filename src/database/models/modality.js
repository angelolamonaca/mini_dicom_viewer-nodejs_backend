module.exports = (sequelize, DataTypes) => {
  const Modality = sequelize.define(
      'Modality',
      {
        name: DataTypes.STRING,
      },
      {
        defaultScope: {
          rawAttributes: { exclude: ['password'] },
        },
      },
  );
  Modality.associate = function (models) {
    // associations can be defined here
    Modality.hasMany(models.Series, { foreignKey: 'idModality', as: 'series' });
  };
  return Modality;
};