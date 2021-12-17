const { Modality, Series} = require('../../database/models');

module.exports = {
    Mutation: {
        async createModality(_, { name }) {
            return Modality.create({
                name
            });
        },
        async deleteModality(_, {id}) {
            return await Modality.destroy(
                {where: {id: id}}
            )
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