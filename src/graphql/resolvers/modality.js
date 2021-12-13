const { Modality } = require('../../database/models');

module.exports = {
    Mutation: {
        async createModality(_, { name }) {
            return Modality.create({
                name
            });
        },
    },

    Query: {
        async getAllModalities(root, args, context) {
            return Modality.findAll();
        },
        async getSingleModality(_, { id }, context) {
            return Modality.findByPk(id);
        },
    },

    Modality: {
        series(modality) {
            return modality.getSeries();
        },
    },
};