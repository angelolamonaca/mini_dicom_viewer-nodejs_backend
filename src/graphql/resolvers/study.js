const {Study} = require('../../database/models');

module.exports = {
    Mutation: {
        async createStudy(_, {studyName, idPatient}) {
            return Study.create({
                studyName,
                idPatient
            });
        },
    },

    Query: {
        async getAllStudies(root, args, context) {
            return Study.findAll();
        },
        async getSingleStudy(_, {id}, context) {
            return Study.findByPk(id);
        },
    },

    Study: {
        series(study) {
            return study.getSeries();
        },
        files(study) {
            return study.getFiles();
        },
    },
};