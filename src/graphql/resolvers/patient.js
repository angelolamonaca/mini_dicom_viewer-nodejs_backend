const { Patient } = require('../../database/models');

module.exports = {
    Mutation: {
        async createPatient(_, { name }) {
            return Patient.create({
                name
            });
        },
    },
};