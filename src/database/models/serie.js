module.exports = (sequelize, DataTypes) => {
    const Series = sequelize.define(
        'Series',
        {
            idPatient: DataTypes.INTEGER,
            idStudy: DataTypes.INTEGER,
            idModality: DataTypes.INTEGER,
            seriesName: DataTypes.STRING,
        },
        {
            defaultScope: {
                rawAttributes: { exclude: ['password'] },
            },
        },
    );
    Series.associate = function (models) {
        // associations can be defined here
        Series.belongsTo(models.Patient, { foreignKey: 'idPatient', as: 'patient' });
        Series.belongsTo(models.Patient, { foreignKey: 'idStudy', as: 'study' });
        Series.belongsTo(models.Patient, { foreignKey: 'idModality', as: 'modality' });
        Series.hasMany(models.File, { foreignKey: 'idSeries', as: 'files' });
    };
    return Series;
};