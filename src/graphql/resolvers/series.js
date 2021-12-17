const {Series, Study} = require('../../database/models');

module.exports = {
    Mutation: {
        async createSeries(_, {seriesName, idPatient, idStudy, idModality}) {
            return await Series.create({
                seriesName,
                idPatient,
                idStudy,
                idModality
            });
        },
        async editSeries(_, {id, seriesName}) {
            return await Series.update(
                {seriesName: seriesName},
                {where: {id: id}}
            )
        },
        async editSeriesModality(_, {id, idModality}) {
            return await Series.update(
                {idModality: idModality},
                {where: {id: id}}
            )
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