const { Patient } = require('../../database/models');

module.exports = {
    Mutation: {
        async createPatient(_, { name }) {
            return Patient.create({
                name
            });
        },
    },

    Query: {
        async getAllPatients(root, args, context) {
            return Patient.findAll();
        },
        async getSinglePatient(_, { patientId }, context) {
            return Patient.findByPk(patientId);
        },
    },

    Patient: {
        studies(patient) {
            return patient.getStudies();
        },
        series(patient) {
            return patient.getSeries();
        },
        files(patient) {
            return patient.getFiles();
        },
    },
};