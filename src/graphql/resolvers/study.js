const { Study } = require('../../database/models');

module.exports = {
    Mutation: {
        async createStudy(_, { studyName , idPatient}) {
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
        async getSingleStudy(_, { studyId }, context) {
            return Study.findByPk(studyId);
        },
    },

    Study: {
        series(Study) {
            return Study.getSeries();
        },
        files(Study) {
            return Study.getFiles();
        },
    },
};