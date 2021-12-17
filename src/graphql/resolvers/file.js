const {File, Series} = require('../../database/models');

module.exports = {
    Mutation: {
        async createFile(_, {filePath, idPatient, idStudy, idSeries}) {
            return await File.create({
                filePath,
                idPatient,
                idStudy,
                idSeries
            });
        },
        async editFile(_, {id, filePath}) {
            return await File.update(
                {filePath: filePath},
                {where: {id: id}}
            )
        },
    },

    Query: {
        async getAllFiles(root, args, context) {
            return File.findAll();
        },
        async getSingleFile(_, {id}, context) {
            return File.findByPk(id);
        },
    }
};