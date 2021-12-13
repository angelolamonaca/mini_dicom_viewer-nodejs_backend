const {File} = require('../../database/models');

module.exports = {
    Mutation: {
        async createFile(_, {filePath, idPatient, idStudy, idSeries}) {
            return File.create({
                filePath,
                idPatient,
                idStudy,
                idSeries
            });
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