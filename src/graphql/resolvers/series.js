const {Series} = require('../../database/models');

module.exports = {
    Mutation: {
        async createSeries(_, {seriesName, idPatient, idStudy, idModality}) {
            return Series.create({
                seriesName,
                idPatient,
                idStudy,
                idModality
            });
        },
    },

    Query: {
        async getAllSeries(root, args, context) {
            return Series.findAll();
        },
        async getSingleSeries(_, {id}, context) {
            return Series.findByPk(id);
        },
    },

    Series: {
        files(series) {
            return series.getFiles();
        },
    },
};