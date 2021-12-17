const {Study, Patient} = require('../../database/models');

module.exports = {
    Mutation: {
        async createStudy(_, {studyName, idPatient}) {
            return await Study.create({
                studyName,
                idPatient
            });
        },
        async editStudy(_, {id, studyName}) {
            return await Study.update(
                {studyName: studyName},
                {where: {id: id}}
            )
        },
        async deleteStudy(_, {id}) {
            return await Study.destroy(
                {where: {id: id}}
            )
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